from app.helpers.typing_helper import LayoutDictTypes
from PySide6.QtCore import QCoreApplication

def tr(text: str) -> str:
    return QCoreApplication.translate("FaceEditorLayout", text)


FACE_EDITOR_LAYOUT_DATA: LayoutDictTypes = {
    '': {
        'FaceEditorCropScaleDecimalSlider': {
            'level': 1,
            'label': tr('Crop Scale'),
            'min_value': '1.50',
            'max_value': '4.00',
            'default': '2.50',
            'step': 0.05,
            'decimals': 2,
            'help': tr('Changes source crop scale. Increase the value to capture the face more distantly. 2.2 scale factor for cropping driving video.')
        },
        'FaceEditorVYRatioDecimalSlider': {
            'level': 1,
            'label': tr('VY Ratio'),
            'min_value': '-0.200',
            'max_value': '0.200',
            'default': '-0.125',
            'step': 0.001,
            'decimals': 3,
            'help': tr('Changes the vy ratio for crop scale. Increase the value to capture the face more distantly. -0.1 factor for cropping driving video.')
        },
        'FaceEditorBlurAmountSlider': {
            'level': 1,
            'label': tr('Blur Amount'),
            'min_value': '0',
            'max_value': '100',
            'default': '5',
            'step': 1,
            'help': tr('Blur amount.')
        },
        'FaceEditorEnableToggle': {
            'level': 1,
            'label': tr('Enable Face Pose/Expression Editor'),
            'default': False,
            'help': tr('Enable Face Pose/Expression Editor.')
        },
        'FaceEditorTypeSelection': {
            'level': 2,
            'label': tr('Face Editor Type'),
            #'options': ['Human-Face', 'Animal-Face'],
            'options': ['Human-Face'],
            'default': 'Human-Face',
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Select the target type to be edited in Face Editor.')
        },
        'EyesOpenRatioDecimalSlider': {
            'level': 2,
            'label': tr('Eyes Close <--> Open Ratio'),
            'min_value': '-0.80',
            'max_value': '0.80',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the opening of the eyes.')
        },
        'LipsOpenRatioDecimalSlider': {
            'level': 2,
            'label': tr('Lips Close <--> Open Ratio'),
            'min_value': '-0.80',
            'max_value': '0.80',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the opening of the lips.')
        },
        'HeadPitchSlider': {
            'level': 2,
            'label': tr('Head Pitch'),
            'min_value': '-15',
            'max_value': '15',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the opening of the lips.')
        },
        'HeadYawSlider': {
            'level': 2,
            'label': tr('Head Yaw'),
            'min_value': '-15',
            'max_value': '15',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the head yaw.')
        },
        'HeadRollSlider': {
            'level': 2,
            'label': tr('Head Roll'),
            'min_value': '-15',
            'max_value': '15',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the head roll.')
        },
        'XAxisMovementDecimalSlider': {
            'level': 2,
            'label': tr('X-Axis Movement'),
            'min_value': '-0.19',
            'max_value': '0.19',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the head direction x-axis.')
        },
        'YAxisMovementDecimalSlider': {
            'level': 2,
            'label': tr('Y-Axis Movement'),
            'min_value': '-0.19',
            'max_value': '0.19',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the head direction y-axis.')
        },
        'ZAxisMovementDecimalSlider': {
            'level': 2,
            'label': tr('Z-Axis Movement'),
            'min_value': '-0.90',
            'max_value': '1.20',
            'default': '1.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the head direction z-axis.')
        },
        'MouthPoutingDecimalSlider': {
            'level': 2,
            'label': tr('Mouth Pouting'),
            'min_value': '-0.09',
            'max_value': '0.09',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Pouting the mouth.')
        },
        'MouthPursingDecimalSlider': {
            'level': 2,
            'label': tr('Mouth Pursing'),
            'min_value': '-20.00',
            'max_value': '15.00',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Pursing the mouth.')
        },
        'MouthGrinDecimalSlider': {
            'level': 2,
            'label': tr('Mouth Grin'),
            'min_value': '0.00',
            'max_value': '15.00',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the mouth grin.')
        },
        'LipsCloseOpenSlider': {
            'level': 2,
            'label': tr('Lips Close <--> Open Value'),
            'min_value': '-90',
            'max_value': '120',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the closing or opening of the lips.')
        },
        'MouthSmileDecimalSlider': {
            'level': 2,
            'label': tr('Mouth Smile'),
            'min_value': '-0.30',
            'max_value': '1.30',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the mouth smile.')
        },
        'EyeWinkDecimalSlider': {
            'level': 2,
            'label': tr('Eye Wink'),
            'min_value': '0.00',
            'max_value': '39.00',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Winking eye.')
        },
        'EyeBrowsDirectionDecimalSlider': {
            'level': 2,
            'label': tr('EyeBrows Direction'),
            'min_value': '-30.00',
            'max_value': '30.00',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the eyebrows direction.')
        },
        'EyeGazeHorizontalDecimalSlider': {
            'level': 2,
            'label': tr('EyeGaze Horizontal'),
            'min_value': '-30.00',
            'max_value': '30.00',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the horizontal eyegaze direction.')
        },
        'EyeGazeVerticalDecimalSlider': {
            'level': 2,
            'label': tr('EyeGaze Vertical'),
            'min_value': '-63.00',
            'max_value': '63.00',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'FaceEditorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the vertical eyegaze direction.')
        },
        'FaceMakeupEnableToggle': {
            'level': 1,
            'label': tr('Face Makeup'),
            'default': False,
            'help': tr('Enable face makeup. Except for hair, eyebrows, eyes and lips.')
        },
        'FaceMakeupRedSlider': {
            'level': 2,
            'label': tr('Red'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Red color adjustments.')
        },
        'FaceMakeupGreenSlider': {
            'level': 2,
            'label': tr('Green'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 3,
            'parentToggle': 'FaceMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Green color adjustments.')
        },
        'FaceMakeupBlueSlider': {
            'level': 2,
            'label': tr('Blue'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blue color adjustments.')
        },
        'FaceMakeupBlendAmountDecimalSlider': {
            'level': 2,
            'label': tr('Blend Amount'),
            'min_value': '0.01',
            'max_value': '1.00',
            'default': '0.05',
            'decimals': 2,
            'step': 0.01,
            'parentToggle': 'FaceMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blend the value: 0.00 represents the original color, 1.00 represents the full target color.')
        },
        'HairMakeupEnableToggle': {
            'level': 1,
            'label': tr('Hair Makeup'),
            'default': False,
            'help': tr('Enable hair makeup.')
        },
        'HairMakeupRedSlider': {
            'level': 2,
            'label': tr('Red'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'HairMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Red color adjustments.')
        },
        'HairMakeupGreenSlider': {
            'level': 2,
            'label': tr('Green'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 3,
            'parentToggle': 'HairMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Green color adjustments.')
        },
        'HairMakeupBlueSlider': {
            'level': 2,
            'label': tr('Blue'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'HairMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blue color adjustments.')
        },
        'HairMakeupBlendAmountDecimalSlider': {
            'level': 2,
            'label': tr('Blend Amount'),
            'min_value': '0.01',
            'max_value': '1.00',
            'default': '0.05',
            'decimals': 2,
            'step': 0.01,
            'parentToggle': 'HairMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blend the value: 0.00 represents the original color, 1.00 represents the full target color.')
        },
        'EyeBrowsMakeupEnableToggle': {
            'level': 1,
            'label': tr('EyeBrows Makeup'),
            'default': False,
            'help': tr('Enable eyebrows makeup.')
        },
        'EyeBrowsMakeupRedSlider': {
            'level': 2,
            'label': tr('Red'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'EyeBrowsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Red color adjustments.')
        },
        'EyeBrowsMakeupGreenSlider': {
            'level': 2,
            'label': tr('Green'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 3,
            'parentToggle': 'EyeBrowsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Green color adjustments.')
        },
        'EyeBrowsMakeupBlueSlider': {
            'level': 2,
            'label': tr('Blue'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'EyeBrowsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blue color adjustments.')
        },
        'EyeBrowsMakeupBlendAmountDecimalSlider': {
            'level': 2,
            'label': tr('Blend Amount'),
            'min_value': '0.01',
            'max_value': '1.00',
            'default': '0.05',
            'decimals': 2,
            'step': 0.01,
            'parentToggle': 'EyeBrowsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blend the value: 0.00 represents the original color, 1.00 represents the full target color.')
        },
        'LipsMakeupEnableToggle': {
            'level': 1,
            'label': tr('Lips Makeup'),
            'default': False,
            'help': tr('Enable lips makeup.')
        },
        'LipsMakeupRedSlider': {
            'level': 2,
            'label': tr('Red'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'LipsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Red color adjustments.')
        },
        'LipsMakeupGreenSlider': {
            'level': 2,
            'label': tr('Green'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 3,
            'parentToggle': 'LipsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Green color adjustments.')
        },
        'LipsMakeupBlueSlider': {
            'level': 2,
            'label': tr('Blue'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'LipsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blue color adjustments.')
        },
        'LipsMakeupBlendAmountDecimalSlider': {
            'level': 2,
            'label': tr('Blend Amount'),
            'min_value': '0.01',
            'max_value': '1.00',
            'default': '0.05',
            'decimals': 2,
            'step': 0.01,
            'parentToggle': 'LipsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blend the value: 0.0 represents the original color, 1.0 represents the full target color.')
        },
    }
}