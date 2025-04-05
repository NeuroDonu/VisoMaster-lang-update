from typing import TYPE_CHECKING
import copy
import os
from functools import partial

import cv2
import numpy
from PIL import Image
from PySide6 import QtGui,QtWidgets,QtCore

if TYPE_CHECKING:
    from app.ui.main_ui import MainWindow
import app.helpers.miscellaneous as misc_helpers
from app.ui.widgets.actions import common_actions as common_widget_actions
from app.ui.widgets.actions import graphics_view_actions
import app.ui.widgets.actions.layout_actions as layout_actions

def set_up_video_seek_line_edit(main_window: 'MainWindow'):
    video_processor = main_window.video_processor
    videoSeekLineEdit = main_window.videoSeekLineEdit
    videoSeekLineEdit.setAlignment(QtCore.Qt.AlignCenter)
    videoSeekLineEdit.setText('0')
    videoSeekLineEdit.setValidator(QtGui.QIntValidator(0, video_processor.max_frame_number))  # Restrict input to numbers 

def set_up_video_seek_slider(main_window: 'MainWindow'):
    class CustomSlider(QtWidgets.QSlider):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.markers = set()
            self.main_window = None
            self._initialized = False

        def initialize(self, main_window):
            if not self._initialized:
                self.main_window = main_window
                self.setMinimum(0)
                self.setMaximum(main_window.video_processor.max_frame_number)
                self.setValue(0)
                self.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
                self._initialized = True

        def paintEvent(self, event):
            # Всегда рисуем базовый слайдер
            super().paintEvent(event)

            # Если нет маркеров, выходим
            if not self.markers:
                return

            # Отрисовываем маркеры
            painter = QtWidgets.QStylePainter(self)
            try:
                opt = QtWidgets.QStyleOptionSlider()
                self.initStyleOption(opt)
                style = self.style()

                # Get groove geometry
                groove_rect = style.subControlRect(
                    QtWidgets.QStyle.ComplexControl.CC_Slider,
                    opt,
                    QtWidgets.QStyle.SubControl.SC_SliderGroove,
                    self
                )

                # Draw markers
                painter.setPen(QtGui.QPen(QtGui.QColor("#e8483c"), 2))
                groove_start = groove_rect.left()
                groove_width = groove_rect.right() - groove_start
                for value in sorted(self.markers):
                    marker_normalized_value = (value - self.minimum()) / (self.maximum() - self.minimum())
                    marker_x = groove_start + marker_normalized_value * groove_width
                    painter.drawLine(marker_x, groove_rect.top(), marker_x, groove_rect.bottom())
            finally:
                painter.end()

    # Проверяем, существует ли уже кастомный слайдер
    if not isinstance(main_window.videoSeekSlider, CustomSlider):
        # Создаем новый слайдер только если текущий не является CustomSlider
        new_slider = CustomSlider(QtCore.Qt.Horizontal)
        new_slider.initialize(main_window)

        # Заменяем старый слайдер новым в layout
        old_slider = main_window.videoSeekSlider
        parent_layout = old_slider.parent()
        layout_pos = parent_layout.layout().indexOf(old_slider)
        parent_layout.layout().removeWidget(old_slider)
        parent_layout.layout().insertWidget(layout_pos, new_slider)

        # Подключаем сигналы к новому слайдеру
        new_slider.valueChanged.connect(lambda value: on_change_video_seek_slider(main_window, value))
        new_slider.sliderMoved.connect(lambda: on_slider_moved(main_window))
        new_slider.sliderPressed.connect(lambda: on_slider_pressed(main_window))
        new_slider.sliderReleased.connect(lambda: on_slider_released(main_window))

        # Добавляем методы для работы с маркерами
        def add_marker_and_paint(self: QtWidgets.QSlider, value=None):
            if value is None or isinstance(value, bool):
                value = self.value()
            if self.minimum() <= value <= self.maximum() and value not in self.markers:
                self.markers.add(value)
                self.update()

        def remove_marker_and_paint(self: QtWidgets.QSlider, value=None):
            if value is None or isinstance(value, bool):
                value = self.value()
            if value in self.markers:
                self.markers.remove(value)
                self.update()

        new_slider.add_marker_and_paint = partial(add_marker_and_paint, new_slider)
        new_slider.remove_marker_and_paint = partial(remove_marker_and_paint, new_slider)

        # Удаляем старый слайдер и сохраняем новый
        old_slider.deleteLater()
        main_window.videoSeekSlider = new_slider
    else:
        # Если слайдер уже является CustomSlider, просто обновляем его состояние
        main_window.videoSeekSlider.initialize(main_window)

def add_video_slider_marker(main_window: 'MainWindow'):
    if main_window.selected_video_button.file_type!='video':
        common_widget_actions.create_and_show_messagebox(main_window, 'Markers Not Available', 'Markers can only be used for videos!', main_window.videoSeekSlider)
        return
    current_position = int(main_window.videoSeekSlider.value())
    # print("current_position", current_position)
    if not main_window.target_faces:
        common_widget_actions.create_and_show_messagebox(main_window, 'No Target Face Found', 'You need to have atleast one target face to create a marker', main_window.videoSeekSlider)
    elif main_window.markers.get(current_position):
        common_widget_actions.create_and_show_messagebox(main_window, 'Marker Already Exists!', 'A Marker already exists for this position!', main_window.videoSeekSlider)
    else:
        add_marker(main_window, copy.deepcopy(main_window.parameters), main_window.control.copy(), current_position)

def remove_video_slider_marker(main_window: 'MainWindow'):
    if main_window.selected_video_button.file_type!='video':
        common_widget_actions.create_and_show_messagebox(main_window, 'Markers Not Available', 'Markers can only be used for videos!', main_window.videoSeekSlider)
        return
    current_position = int(main_window.videoSeekSlider.value())
    # print("current_position", current_position)
    if main_window.markers.get(current_position):
        remove_marker(main_window, current_position)
    else:
        common_widget_actions.create_and_show_messagebox(main_window, 'No Marker Found!', 'No Marker Found for this position!', main_window.videoSeekSlider)

def add_marker(main_window: 'MainWindow', parameters, control, position,):
    main_window.videoSeekSlider.add_marker_and_paint(position)
    main_window.markers[position] = {'parameters': parameters, 'control': control}
    print(f"Marker Added for Frame: {position}")

def remove_marker(main_window: 'MainWindow', position):
    if main_window.markers.get(position):
        main_window.videoSeekSlider.remove_marker_and_paint(position)
        main_window.markers.pop(position)
        print(f"Marker Removed from position: {position}")

def remove_all_markers(main_window: 'MainWindow'):
    for marker_position in list(main_window.markers.keys()):
        remove_marker(main_window, marker_position)

def move_slider_to_nearest_marker(main_window: 'MainWindow', direction: str):
    """
    Move the slider to the nearest marker in the specified direction.

    :param direction: 'next' to move to the next marker, 'previous' to move to the previous marker.
    """
    new_position = None
    current_position = int(main_window.videoSeekSlider.value())
    markers = sorted(main_window.markers.keys())
    if direction == "next":
        filtered_markers = [marker for marker in markers if marker > current_position]
        new_position = filtered_markers[0] if filtered_markers else None
    elif direction == "previous":
        filtered_markers = [marker for marker in markers if marker < current_position]
        new_position = filtered_markers[-1] if filtered_markers else None

    if new_position is not None:
        main_window.videoSeekSlider.setValue(new_position)
        main_window.video_processor.process_current_frame()

# Wrappers for specific directions
def move_slider_to_next_nearest_marker(main_window: 'MainWindow'):
    move_slider_to_nearest_marker(main_window, "next")

def move_slider_to_previous_nearest_marker(main_window: 'MainWindow'):
    move_slider_to_nearest_marker(main_window, "previous")

def remove_face_parameters_and_control_from_markers(main_window: 'MainWindow', face_id):
    for _, marker_data in main_window.markers.items():
        marker_data['parameters'].pop(face_id)
        # If the parameters is empty, then there is no longer any marker to be set for any target face
        if not marker_data['parameters']:
            delete_all_markers(main_window)
            break

def advance_video_slider_by_n_frames(main_window: 'MainWindow', n=30):
    video_processor = main_window.video_processor
    if video_processor.media_capture:
        current_position = int(main_window.videoSeekSlider.value())
        new_position = current_position + n
        if new_position > video_processor.max_frame_number:
            new_position = video_processor.max_frame_number
        main_window.videoSeekSlider.setValue(new_position)
        main_window.video_processor.process_current_frame()

def rewind_video_slider_by_n_frames(main_window: 'MainWindow', n=30):
    video_processor = main_window.video_processor
    if video_processor.media_capture:
        current_position = int(main_window.videoSeekSlider.value())
        new_position = current_position - n
        if new_position < 0:
            new_position = 0
        main_window.videoSeekSlider.setValue(new_position)
        main_window.video_processor.process_current_frame()

def delete_all_markers(main_window: 'MainWindow'):
    main_window.videoSeekSlider.markers = set()
    main_window.videoSeekSlider.update()
    main_window.markers = {}

def view_fullscreen(main_window: 'MainWindow'):

    if main_window.is_full_screen:
        main_window.showNormal()  # Exit full-screen mode
        main_window.menuBar().show()
    else:
        main_window.showFullScreen()  # Enter full-screen mode
        main_window.menuBar().hide()

    main_window.is_full_screen = not main_window.is_full_screen

def enable_zoom_and_pan(view: QtWidgets.QGraphicsView):
    SCALE_FACTOR = 1.1
    view.zoom_value = 0  # Track zoom level
    view.last_scale_factor = 1.0  # Track the last scale factor (1.0 = no scaling)
    view.is_panning = False  # Track whether panning is active
    view.pan_start_pos = QtCore.QPoint()  # Store the initial mouse position for panning

    def zoom(self:QtWidgets.QGraphicsView, step=False):
        """Zoom in or out by a step."""
        if not step:
            factor = self.last_scale_factor
        else:
            self.zoom_value += step
            factor = SCALE_FACTOR ** step
            self.last_scale_factor *= factor  # Update the last scale factor
        if factor > 0:
            self.scale(factor, factor)

    def wheelEvent(self:QtWidgets.QGraphicsView, event:QtGui.QWheelEvent):
        """Handle mouse wheel event for zooming."""
        delta = event.angleDelta().y()
        if delta != 0:
            zoom(self, delta // abs(delta))
    
    def reset_zoom(self:QtWidgets.QGraphicsView):
        # print("Called reset_zoom()")
        # Reset zoom level to fit the view.
        self.zoom_value = 0
        if not self.scene():
            return
        items = self.scene().items()
        if not items:
            return
        rect = self.scene().itemsBoundingRect()
        self.setSceneRect(rect)
        unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
        self.scale(1 / unity.width(), 1 / unity.height())
        view_rect = self.viewport().rect()
        scene_rect = self.transform().mapRect(rect)
        factor = min(view_rect.width() / scene_rect.width(),
                    view_rect.height() / scene_rect.height())
        self.scale(factor, factor)

    def mousePressEvent(self: QtWidgets.QGraphicsView, event: QtGui.QMouseEvent):
        """Handle mouse press event for panning."""
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self.is_panning = True
            self.pan_start_pos = event.pos()  # Store the initial mouse position
            self.setCursor(QtCore.Qt.ClosedHandCursor)  # Change cursor to indicate panning
        else:
            # Explicitly call the base class implementation
            QtWidgets.QGraphicsView.mousePressEvent(self, event)

    def mouseMoveEvent(self: QtWidgets.QGraphicsView, event: QtGui.QMouseEvent):
        """Handle mouse move event for panning."""
        if self.is_panning:
            # Calculate the distance moved
            delta = event.pos() - self.pan_start_pos
            self.pan_start_pos = event.pos()  # Update the start position
            # Translate the view
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())
        else:
            # Explicitly call the base class implementation
            QtWidgets.QGraphicsView.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self: QtWidgets.QGraphicsView, event: QtGui.QMouseEvent):
        """Handle mouse release event for panning."""
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self.is_panning = False
            self.setCursor(QtCore.Qt.ArrowCursor)  # Reset the cursor
        else:
            # Explicitly call the base class implementation
            QtWidgets.QGraphicsView.mouseReleaseEvent(self, event)

    # Attach methods to the view
    view.zoom = partial(zoom, view)
    view.reset_zoom = partial(reset_zoom, view)
    view.wheelEvent = partial(wheelEvent, view)
    view.mousePressEvent = partial(mousePressEvent, view)
    view.mouseMoveEvent = partial(mouseMoveEvent, view)
    view.mouseReleaseEvent = partial(mouseReleaseEvent, view)

    # view.zoom = zoom.__get__(view)
    # view.reset_zoom = reset_zoom.__get__(view)
    # view.wheelEvent = wheelEvent.__get__(view)

    # Set anchors for better interaction
    view.setTransformationAnchor(QtWidgets.QGraphicsView.ViewportAnchor.AnchorUnderMouse)
    view.setResizeAnchor(QtWidgets.QGraphicsView.ViewportAnchor.AnchorUnderMouse)


def play_video(main_window: 'MainWindow', checked: bool):
    video_processor = main_window.video_processor
    if checked:
        if video_processor.processing or video_processor.current_frame_number==video_processor.max_frame_number:
            print("play_video: Video already playing. Stopping the current video before starting a new one.")
            video_processor.stop_processing()
            return
        print("play_video: Starting video processing.")
        set_play_button_icon_to_stop(main_window)
        video_processor.process_video()
    else:
        video_processor = main_window.video_processor
        # print("play_video: Stopping video processing.")
        set_play_button_icon_to_play(main_window)
        video_processor.stop_processing()
        main_window.buttonMediaRecord.blockSignals(True)
        main_window.buttonMediaRecord.setChecked(False)
        main_window.buttonMediaRecord.blockSignals(False)
        set_record_button_icon_to_play(main_window)


def record_video(main_window: 'MainWindow', checked: bool):
    video_processor = main_window.video_processor
    # Dont record webcam capture
    if video_processor.file_type == 'webcam':
        main_window.buttonMediaRecord.blockSignals(True)
        main_window.buttonMediaRecord.setChecked(not checked)
        main_window.buttonMediaRecord.blockSignals(False)
        return
    
    if checked:
        if video_processor.processing or video_processor.current_frame_number==video_processor.max_frame_number:
            print("record_video: Video already playing. Stopping the current video before starting a new one.")
            video_processor.stop_processing()
            return
        if not main_window.control.get('OutputMediaFolder','').strip():
            common_widget_actions.create_and_show_messagebox(main_window, 'No Output Folder Selected','Please select an Output folder to save the Videos before recording!', main_window)
            main_window.buttonMediaRecord.setChecked(False)
            return
        if not misc_helpers.is_ffmpeg_in_path():
            common_widget_actions.create_and_show_messagebox(main_window, 'FFMPEG Not Found','FFMPEG was not found in your system. Check your installation!', main_window)
            main_window.buttonMediaRecord.setChecked(False)
            return
        video_processor.recording = True
        main_window.buttonMediaPlay.setChecked(True)
        set_record_button_icon_to_stop(main_window)

    else:
        main_window.buttonMediaPlay.setChecked(False)
        video_processor.stop_processing()
        set_play_button_icon_to_play(main_window)
        set_record_button_icon_to_play(main_window)

def set_record_button_icon_to_play(main_window: 'MainWindow'):
    main_window.buttonMediaRecord.setIcon(QtGui.QIcon(":/media/media/rec_off.png"))
    main_window.buttonMediaRecord.setToolTip("Start Recording")
def set_record_button_icon_to_stop(main_window: 'MainWindow'):
    main_window.buttonMediaRecord.setIcon(QtGui.QIcon(":/media/media/rec_on.png"))
    main_window.buttonMediaRecord.setToolTip("Stop Recording")

def set_play_button_icon_to_play(main_window: 'MainWindow'):
    main_window.buttonMediaPlay.setIcon(QtGui.QIcon(":/media/media/play_off.png"))
    main_window.buttonMediaPlay.setToolTip("Play")

def set_play_button_icon_to_stop(main_window: 'MainWindow'):
    main_window.buttonMediaPlay.setIcon(QtGui.QIcon(":/media/media/play_on.png"))
    main_window.buttonMediaPlay.setToolTip("Stop")

def reset_media_buttons(main_window: 'MainWindow'):
    # Rest the state and icons of the buttons without triggering Onchange methods
    main_window.buttonMediaPlay.blockSignals(True)
    main_window.buttonMediaPlay.setChecked(False)
    main_window.buttonMediaPlay.blockSignals(False)
    main_window.buttonMediaRecord.blockSignals(True)
    main_window.buttonMediaRecord.setChecked(False)
    main_window.buttonMediaRecord.blockSignals(False)
    set_play_button_icon(main_window)
    set_record_button_icon(main_window)


def set_play_button_icon(main_window: 'MainWindow'):
    if main_window.buttonMediaPlay.isChecked(): 
        main_window.buttonMediaPlay.setIcon(QtGui.QIcon(":/media/media/play_on.png"))
        main_window.buttonMediaPlay.setToolTip("Stop")
    else:
        main_window.buttonMediaPlay.setIcon(QtGui.QIcon(":/media/media/play_off.png"))
        main_window.buttonMediaPlay.setToolTip("Play")

def set_record_button_icon(main_window: 'MainWindow'):
    if main_window.buttonMediaRecord.isChecked(): 
        main_window.buttonMediaRecord.setIcon(QtGui.QIcon(":/media/media/rec_on.png"))
        main_window.buttonMediaRecord.setToolTip("Stop Recording")
    else:
        main_window.buttonMediaRecord.setIcon(QtGui.QIcon(":/media/media/rec_off.png"))
        main_window.buttonMediaRecord.setToolTip("Start Recording")

# @misc_helpers.benchmark
@QtCore.Slot(int)
def on_change_video_seek_slider(main_window: 'MainWindow', new_position=0):
    # print("Called on_change_video_seek_slider()")
    video_processor = main_window.video_processor

    was_processing = video_processor.stop_processing()
    if was_processing:
        print("on_change_video_seek_slider: Processing in progress. Stopping current processing.")

    video_processor.current_frame_number = new_position
    video_processor.next_frame_to_display = new_position
    if video_processor.media_capture:
        video_processor.media_capture.set(cv2.CAP_PROP_POS_FRAMES, new_position)
        ret, frame = misc_helpers.read_frame(video_processor.media_capture)
        if ret:
            pixmap = common_widget_actions.get_pixmap_from_frame(main_window, frame)
            graphics_view_actions.update_graphics_view(main_window, pixmap, new_position)
            if video_processor.current_frame_number == video_processor.max_frame_number:
                video_processor.media_capture.set(cv2.CAP_PROP_POS_FRAMES, new_position)
            update_parameters_and_control_from_marker(main_window, new_position)
            update_widget_values_from_markers(main_window, new_position)

    # Do not automatically restart the video, let the user press Play to resume
    # print("on_change_video_seek_slider: Video stopped after slider movement.")

def update_parameters_and_control_from_marker(main_window: 'MainWindow', new_position: int):
    if main_window.markers.get(new_position):
        main_window.parameters = copy.deepcopy(main_window.markers[new_position]['parameters'])
        main_window.control.update(main_window.markers[new_position]['control'].copy())

def update_widget_values_from_markers(main_window: 'MainWindow', new_position: int):
    if main_window.markers.get(new_position):
        if main_window.selected_target_face_id is not None:
            common_widget_actions.set_widgets_values_using_face_id_parameters(main_window, main_window.selected_target_face_id)
            common_widget_actions.set_control_widgets_values(main_window, enable_exec_func=False)

def on_slider_moved(main_window: 'MainWindow'):
    # print("Called on_slider_moved()")
    position = main_window.videoSeekSlider.value()
    # print(f"\nSlider Moved. position: {position}\n")

def on_slider_pressed(main_window: 'MainWindow'):

    position = main_window.videoSeekSlider.value()
    # print(f"\nSlider Pressed. position: {position}\n")

# @misc_helpers.benchmark
def on_slider_released(main_window: 'MainWindow'):
    # print("Called on_slider_released()")

    new_position = main_window.videoSeekSlider.value()
    # print(f"\nSlider released. New position: {new_position}\n")
    # Perform the update to the new frame
    video_processor = main_window.video_processor
    if video_processor.media_capture:
        video_processor.process_current_frame()  # Process the current frame

def process_swap_faces(main_window: 'MainWindow'):
    video_processor = main_window.video_processor
    video_processor.process_current_frame()

def process_edit_faces(main_window: 'MainWindow'):
    video_processor = main_window.video_processor
    video_processor.process_current_frame()

def process_compare_checkboxes(main_window: 'MainWindow'):
    main_window.video_processor.process_current_frame()
    layout_actions.fit_image_to_view_onchange(main_window)

def save_current_frame_to_file(main_window: 'MainWindow'):
    if not main_window.outputFolderLineEdit.text():
        common_widget_actions.create_and_show_messagebox(main_window, 'No Output Folder Selected','Please select an Output folder to save the Images/Videos before Saving/Recording!', main_window)
        return
    frame = main_window.video_processor.current_frame.copy()
    if isinstance(frame, numpy.ndarray):
        # save_filename, _ = os.path.splitext(main_window.video_processor.media_path)
        # save_filename, _ = QtWidgets.QFileDialog.getSaveFileName(main_window, 'Save Frame as Image', f'{save_filename}.png', filter='PNG (*.png)',)
        save_filename = misc_helpers.get_output_file_path(main_window.video_processor.media_path, main_window.control['OutputMediaFolder'], media_type='image')
        if save_filename:
            pil_image = Image.fromarray(frame[..., ::-1])
            pil_image.save(save_filename, 'PNG')
            common_widget_actions.create_and_show_toast_message(main_window, 'Image Saved', f'Saved Current Image to file: {save_filename}')

    else:
        common_widget_actions.create_and_show_messagebox(main_window, 'Invalid Frame', 'Cannot save the current frame!', parent_widget=main_window.saveImageButton)
