from app.ui.widgets.actions import control_actions
import cv2
from app.helpers.typing_helper import LayoutDictTypes
from PySide6.QtCore import QCoreApplication

def tr(text: str) -> str:
    return QCoreApplication.translate("SettingsLayout", text)

SETTINGS_LAYOUT_DATA: LayoutDictTypes = {
    tr('Appearance'): {
        'ThemeSelection': {
            'level': 1,
            'label': tr('Theme'),
            'options': [tr('Dark'), tr('Dark-Blue'), tr('Light')],
            'default': 'Dark',
            'help': tr('Select the theme to be used'),
            'exec_function': control_actions.change_theme,
            'exec_function_args': [],
        },
    },
    tr('General'): {
        'ProvidersPrioritySelection': {
            'level': 1,
            'label': tr('Providers Priority'),
            'options': ['CUDA', 'TensorRT', 'TensorRT-Engine', 'CPU'],
            'default': 'CUDA',
            'help': tr('Select the providers priority to be used with the system.'),
            'exec_function': control_actions.change_execution_provider,
            'exec_function_args': [],
        },
        'nThreadsSlider': {
            'level': 1,
            'label': tr('Number of Threads'),
            'min_value': '1',
            'max_value': '30',
            'default': '2',
            'step': 1,
            'help': tr('Set number of execution threads while playing and recording. Depends strongly on GPU VRAM.'),
            'exec_function': control_actions.change_threads_number,
            'exec_function_args': [],
        },
    },
    tr('Video Settings'): {
        'VideoPlaybackCustomFpsToggle': {
            'level': 1,
            'label': tr('Set Custom Video Playback FPS'),
            'default': False,
            'help': tr('Manually set the FPS to be used when playing the video'),
            'exec_function': control_actions.set_video_playback_fps,
            'exec_function_args': [],
        },
        'VideoPlaybackCustomFpsSlider': {
            'level': 2,
            'label': tr('Video Playback FPS'),
            'min_value': '1',
            'max_value': '120',
            'default': '30',
            'parentToggle': 'VideoPlaybackCustomFpsToggle',
            'requiredToggleValue': True,
            'step': 1,
            'help': tr('Set the maximum FPS of the video when playing')
        },
    },
    tr('Auto Swap'): {
        'AutoSwapToggle': {
            'level': 1,
            'label': tr('Auto Swap'),
            'default': False,
            'help': tr('Automatically Swap all faces using selected Source Faces/Embeddings when loading an video/image file')
        },
    },
    tr('Detectors'): {
        'DetectorModelSelection': {
            'level': 1,
            'label': tr('Face Detect Model'),
            'options': ['RetinaFace', 'Yolov8', 'SCRFD', 'Yunet'],
            'default': 'RetinaFace',
            'help': tr('Select the face detection model to use for detecting faces in the input image or video.')
        },
        'DetectorScoreSlider': {
            'level': 1,
            'label': tr('Detect Score'),
            'min_value': '1',
            'max_value': '100',
            'default': '50',
            'step': 1,
            'help': tr('Set the confidence score threshold for face detection. Higher values ensure more confident detections but may miss some faces.')
        },
        'MaxFacesToDetectSlider': {
            'level': 1,
            'label': tr('Max No of Faces to Detect'),
            'min_value': '1',
            'max_value': '50',
            'default': '20',
            'step': 1,     
            'help': tr('Set the maximum number of faces to detect in a frame')
        },
        'AutoRotationToggle': {
            'level': 1,
            'label': tr('Auto Rotation'),
            'default': False,
            'help': tr('Automatically rotate the input to detect faces in various orientations.')
        },
        'ManualRotationEnableToggle': {
            'level': 1,
            'label': tr('Manual Rotation'),
            'default': False,
            'help': tr('Rotate the face detector to better detect faces at different angles.')
        },
        'ManualRotationAngleSlider': {
            'level': 2,
            'label': tr('Rotation Angle'),
            'min_value': '0',
            'max_value': '270',
            'default': '0',
            'step': 90,
            'parentToggle': 'ManualRotationEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Set this to the angle of the input face angle to help with laying down/upside down/etc. Angles are read clockwise.')
        },
        'LandmarkDetectToggle': {
            'level': 1,
            'label': tr('Enable Landmark Detection'),
            'default': False,
            'help': tr('Enable or disable facial landmark detection, which is used to refine face alignment.')
        },
        'LandmarkDetectModelSelection': {
            'level': 2,
            'label': tr('Landmark Detect Model'),
            'options': ['5', '68', '3d68', '98', '106', '203', '478'],
            'default': '203',
            'parentToggle': 'LandmarkDetectToggle',
            'requiredToggleValue': True,
            'help': tr('Select the landmark detection model, where different models detect varying numbers of facial landmarks.')
        },
        'LandmarkDetectScoreSlider': {
            'level': 2,
            'label': tr('Landmark Detect Score'),
            'min_value': '1',
            'max_value': '100',
            'default': '50',
            'step': 1,
            'parentToggle': 'LandmarkDetectToggle',
            'requiredToggleValue': True,
            'help': tr('Set the confidence score threshold for facial landmark detection.')
        },
        'DetectFromPointsToggle': {
            'level': 2,
            'label': tr('Detect From Points'),
            'default': False,
            'parentToggle': 'LandmarkDetectToggle',
            'requiredToggleValue': True,
            'help': tr('Enable detection of faces from specified landmark points.')
        },
        'ShowLandmarksEnableToggle': {
            'level': 1,
            'label': tr('Show Landmarks'),
            'default': False,
            'help': tr('Show Landmarks in realtime.')
        },
        'ShowAllDetectedFacesBBoxToggle': {
            'level': 1,
            'label': tr('Show Bounding Boxes'),
            'default': False,
            'help': tr('Draw bounding boxes to all detected faces in the frame')
        }
    },
    tr('DFM Settings'): {
        'MaxDFMModelsSlider': {
            'level': 1,
            'label': tr('Maximum DFM Models to use'),
            'min_value': '1',
            'max_value': '5',
            'default': '1',
            'step': 1,
            'help': tr("Set the maximum number of DFM Models to keep in memory at a time. Set this based on your GPU's VRAM"),
        }
    },
    tr('Frame Enhancer'): {
        'FrameEnhancerEnableToggle': {
            'level': 1,
            'label': tr('Enable Frame Enhancer'),
            'default': False,
            'help': tr('Enable frame enhancement for video inputs to improve visual quality.')
        },
        'FrameEnhancerTypeSelection': {
            'level': 2,
            'label': tr('Frame Enhancer Type'),
            'options': ['RealEsrgan-x2-Plus', 'RealEsrgan-x4-Plus', 'RealEsr-General-x4v3', 'BSRGan-x2', 'BSRGan-x4', 'UltraSharp-x4', 'UltraMix-x4', 'DDColor-Artistic', 'DDColor', 'DeOldify-Artistic', 'DeOldify-Stable', 'DeOldify-Video'],
            'default': 'RealEsrgan-x2-Plus',
            'parentToggle': 'FrameEnhancerEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Select the type of frame enhancement to apply, based on the content and resolution requirements.')
        },
        'FrameEnhancerBlendSlider': {
            'level': 2,
            'label': tr('Blend'),
            'min_value': '0',
            'max_value': '100',
            'default': '100',
            'step': 1,
            'parentToggle': 'FrameEnhancerEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blends the enhanced results back into the original frame.')
        },
    },
    tr('Webcam Settings'): {
        'WebcamMaxNoSelection': {
            'level': 2,
            'label': tr('Webcam Max No'),
            'options': ['1', '2', '3', '4', '5', '6'],
            'default': '1',
            'help': tr('Select the maximum number of webcam streams to allow for face swapping.')
        },
        'WebcamBackendSelection': {
            'level': 2,
            'label': tr('Webcam Backend'),
            'options': [tr('Default'), tr('DirectShow'), tr('MSMF'), tr('V4L'), tr('V4L2'), tr('GSTREAMER')],
            'default': tr('Default'),
            'help': tr('Choose the backend for accessing webcam input.')
        },
        'WebcamMaxResSelection': {
            'level': 2,
            'label': tr('Webcam Resolution'),
            'options': ['480x360', '640x480', '1280x720', '1920x1080', '2560x1440', '3840x2160'],
            'default': '1280x720',
            'help': tr('Select the maximum resolution for webcam input.')
        },
        'WebCamMaxFPSSelection': {
            'level': 2,
            'label': tr('Webcam FPS'),
            'options': ['23', '30', '60'],
            'default': '30',
            'help': tr('Set the maximum frames per second (FPS) for webcam input.')
        },
    },
    tr('Virtual Camera'): {
        'SendVirtCamFramesEnableToggle': {
            'level': 1,
            'label': tr('Send Frames to Virtual Camera'),
            'default': False,
            'help': tr('Send the swapped video/webcam output to virtual camera for using in external applications'),
            'exec_function': control_actions.toggle_virtualcam,
            'exec_function_args': [],
        },
        'VirtCamBackendSelection': {
            'level': 1,
            'label': tr('Virtual Camera Backend'),
            'options': ['obs', 'unitycapture'],
            'default': 'obs',
            'help': tr('Choose the backend based on the Virtual Camera you have set up'),
            'parentToggle': 'SendVirtCamFramesEnableToggle',
            'requiredToggleValue': True,
            'exec_function': control_actions.enable_virtualcam,
            'exec_funtion_args': [],
        },
    },
    tr('Face Recognition'): {
        'RecognitionModelSelection': {
            'level': 1,
            'label': tr('Recognition Model'),
            'options': ['Inswapper128ArcFace', 'SimSwapArcFace', 'GhostArcFace', 'CSCSArcFace'],
            'default': 'Inswapper128ArcFace',
            'help': tr('Choose the ArcFace model to be used for comparing the similarity of faces.')
        },
        'SimilarityTypeSelection': {
            'level': 1,
            'label': tr('Swapping Similarity Type'),
            'options': [tr('Opal'), tr('Pearl'), tr('Optimal')],
            'default': tr('Opal'),
            'help': tr('Choose the type of similarity calculation for face detection and matching during the face swapping process.')
        },
    },
    tr('Embedding Merge Method'): {
        'EmbMergeMethodSelection': {
            'level': 1,
            'label': tr('Embedding Merge Method'),
            'options': [tr('Mean'), tr('Median')],
            'default': tr('Mean'),
            'help': tr('Select the method to merge facial embeddings. "Mean" averages the embeddings, while "Median" selects the middle value, providing more robustness to outliers.')
        }
    },
    tr('Media Selection'): {
        'TargetMediaFolderRecursiveToggle': {
            'level': 1,
            'label': tr('Target Media Include Subfolders'),
            'default': False,
            'help': tr('Include all files from Subfolders when choosing Target Media Folder')
        },
        'InputFacesFolderRecursiveToggle': {
            'level': 1,
            'label': tr('Input Faces Include Subfolders'),
            'default': False,
            'help': tr('Include all files from Subfolders when choosing Input Faces Folder')
        }
    }
}

CAMERA_BACKENDS = {
    'Default': cv2.CAP_ANY,
    'DirectShow': cv2.CAP_DSHOW,
    'MSMF': cv2.CAP_MSMF,
    'V4L': cv2.CAP_V4L,
    'V4L2': cv2.CAP_V4L2,
    'GSTREAMER': cv2.CAP_GSTREAMER,
}