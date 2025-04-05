from app.helpers import miscellaneous as misc_helpers
from app.ui.widgets.actions import layout_actions
from app.helpers.typing_helper import LayoutDictTypes
from PySide6.QtCore import QCoreApplication

def tr(text: str) -> str:
    return QCoreApplication.translate("SwapperLayout", text)

# Widgets in Face Swap tab are created from this Layout
SWAPPER_LAYOUT_DATA: LayoutDictTypes = {
    tr('Swapper'): {
        'SwapModelSelection': {
            'level': 1,
            'label': tr('Swapper Model'),
            'options': ['Inswapper128', 'InStyleSwapper256 Version A', 'InStyleSwapper256 Version B', 'InStyleSwapper256 Version C', 'DeepFaceLive (DFM)', 'SimSwap512', 'GhostFace-v1', 'GhostFace-v2', 'GhostFace-v3', 'CSCS'],            'default': 'Inswapper128',
            'help': tr('Choose which swapper model to use for face swapping.')
        },
        'SwapperResSelection': {
            'level': 2,
            'label': tr('Swapper Resolution'),
            'options': ['128', '256', '384', '512'],
            'default': '128',
            'parentSelection': 'SwapModelSelection',
            'requiredSelectionValue': 'Inswapper128',
            'help': tr('Select the resolution for the swapped face in pixels. Higher values offer better quality but are slower to process.')
        },
        'DFMModelSelection': {
            'level': 2,
            'label': tr('DFM Model'),
            'options': misc_helpers.get_dfm_models_selection_values,
            'default': misc_helpers.get_dfm_models_default_value,
            'parentSelection': 'SwapModelSelection',
            'requiredSelectionValue': 'DeepFaceLive (DFM)',
            'help': tr('Select which pretrained DeepFaceLive (DFM) Model to use for swapping.')
        },
        'DFMAmpMorphSlider': {
            'level': 2,
            'label': tr('AMP Morph Factor'),
            'min_value': '1',
            'max_value': '100',
            'default': '50',
            'step': 1,
            'parentSelection': 'SwapModelSelection',
            'requiredSelectionValue': 'DeepFaceLive (DFM)',
            'help': tr('AMP Morph Factor for DFM AMP Models'),
        },
        'DFMRCTColorToggle': {
            'level': 2,
            'label': tr('RCT Color Transfer'),
            'default': False,
            'parentSelection': 'SwapModelSelection',
            'requiredSelectionValue': 'DeepFaceLive (DFM)',
            'help': tr('RCT Color Transfer for DFM Models'),
        }
    },
    tr('Face Landmarks Correction'): {
        'FaceAdjEnableToggle': {
            'level': 1,
            'label': tr('Face Adjustments'),
            'default': False,
            'help': tr('This is an experimental feature to perform direct adjustments to the face landmarks found by the detector. There is also an option to adjust the scale of the swapped face.')
        },
        'KpsXSlider': {
            'level': 2,
            'label': tr('Keypoints X-Axis'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the detection points left and right.')
        },
        'KpsYSlider': {
            'level': 2,
            'label': tr('Keypoints Y-Axis'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the detection points up and down.')
        },
        'KpsScaleSlider': {
            'level': 2,
            'label': tr('Keypoints Scale'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Grows and shrinks the detection point distances.')
        },
        'FaceScaleAmountSlider': {
            'level': 2,
            'label': tr('Face Scale Amount'),
            'min_value': '-20',
            'max_value': '20',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Grows and shrinks the entire face.')
        },
        'LandmarksPositionAdjEnableToggle': {
            'level': 1,
            'label': tr('5 - Keypoints Adjustments'),
            'default': False,
            'help': tr('This is an experimental feature to perform direct adjustments to the position of face landmarks found by the detector.')
        },
        'EyeLeftXAmountSlider': {
            'level': 2,
            'label': tr('Left Eye:   X'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'LandmarksPositionAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the eye left detection point left and right.')
        },
        'EyeLeftYAmountSlider': {
            'level': 2,
            'label': tr('Left Eye:   Y'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'LandmarksPositionAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the eye left detection point up and down.')
        },
        'EyeRightXAmountSlider': {
            'level': 2,
            'label': tr('Right Eye:   X'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'LandmarksPositionAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the eye right detection point left and right.')
        },
        'EyeRightYAmountSlider': {
            'level': 2,
            'label': tr('Right Eye:   Y'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'LandmarksPositionAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the eye right detection point up and down.')
        },
        'NoseXAmountSlider': {
            'level': 2,
            'label': tr('Nose:   X'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'LandmarksPositionAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the nose detection point left and right.')
        },
        'NoseYAmountSlider': {
            'level': 2,
            'label': tr('Nose:   Y'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'LandmarksPositionAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the nose detection point up and down.')
        },
        'MouthLeftXAmountSlider': {
            'level': 2,
            'label': tr('Left Mouth:   X'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'LandmarksPositionAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the mouth left detection point left and right.')
        },
        'MouthLeftYAmountSlider': {
            'level': 2,
            'label': tr('Left Mouth:   Y'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'LandmarksPositionAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the mouth left detection point up and down.')
        },
        'MouthRightXAmountSlider': {
            'level': 2,
            'label': tr('Right Mouth:   X'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'LandmarksPositionAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the mouth Right detection point left and right.')
        },
        'MouthRightYAmountSlider': {
            'level': 2,
            'label': tr('Right Mouth:   Y'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'LandmarksPositionAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Shifts the mouth Right detection point up and down.')
        },
    },
    tr('Face Similarity'): {
        'SimilarityThresholdSlider': {
            'level': 1,
            'label': tr('Similarity Threshold'),
            'min_value': '1',
            'max_value': '100',
            'default': '60',
            'step': 1,
            'help': tr('Set the similarity threshold to control how similar the detected face should be to the reference (target) face.')
        },
        'StrengthEnableToggle': {
            'level': 1,
            'label': tr('Strength'),
            'default': False,
            'help': tr('Apply additional swapping iterations to increase the strength of the result, which may increase likeness.')
        },
        'StrengthAmountSlider': {
            'level': 2,
            'label': tr('Amount'),
            'min_value': '0',
            'max_value': '500',
            'default': '100',
            'step': 25,
            'parentToggle': 'StrengthEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Increase up to 5x additional swaps (500%). 200% is generally a good result. Set to 0 to turn off swapping but allow the rest of the pipeline to apply to the original image.')
        },
        'FaceLikenessEnableToggle': {
            'level': 1,
            'label': tr('Face Likeness'),
            'default': False,
            'help': tr('This is a feature to perform direct adjustments to likeness of faces.')
        },
        'FaceLikenessFactorDecimalSlider': {
            'level': 2,
            'label': tr('Amount'),
            'min_value': '-1.00',
            'max_value': '1.00',
            'default': '0.00',
            'decimals': 2,
            'step': 0.05,
            'parentToggle': 'FaceLikenessEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Determines the factor of likeness between the source and assigned faces.')
        },
        'DifferencingEnableToggle': {
            'level': 1,
            'label': tr('Differencing'),
            'default': False,
            'help': tr('Allow some of the original face to show in the swapped result when the difference between the two images is small. Can help bring back some texture to the swapped face.')
        },
        'DifferencingAmountSlider': {
            'level': 2,
            'label': tr('Amount'),
            'min_value': '0',
            'max_value': '100',
            'default': '4',
            'step': 1,
            'parentToggle': 'DifferencingEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Higher values relaxes the similarity constraint.')
        },
        'DifferencingBlendAmountSlider': {
            'level': 2,
            'label': tr('Blend Amount'),
            'min_value': '0',
            'max_value': '100',
            'default': '5',
            'step': 1,
            'parentToggle': 'DifferencingEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blend differecing value.')
        },
    },
    tr('Face Mask'):{
        'BorderBottomSlider':{
            'level': 1,
            'label': tr('Bottom Border'),
            'min_value': '0',
            'max_value': '100',
            'default': '10',
            'step': 1,
            'help': tr('A rectangle with adjustable bottom, left, right, top, and sides that masks the swapped face result back into the original image.')
        },
        'BorderLeftSlider':{
            'level': 1,
            'label': tr('Left Border'),
            'min_value': '0',
            'max_value': '100',
            'default': '10',
            'step': 1,
            'help': tr('A rectangle with adjustable bottom, left, right, top, and sides that masks the swapped face result back into the original image.')
        },
        'BorderRightSlider':{
            'level': 1,
            'label': tr('Right Border'),
            'min_value': '0',
            'max_value': '100',
            'default': '10',
            'step': 1,
            'help': tr('A rectangle with adjustable bottom, left, right, top, and sides that masks the swapped face result back into the original image.')
        },
        'BorderTopSlider':{
            'level': 1,
            'label': tr('Top Border'),
            'min_value': '0',
            'max_value': '100',
            'default': '10',
            'step': 1,
            'help': tr('A rectangle with adjustable bottom, left, right, top, and sides that masks the swapped face result back into the original image.')
        },
        'BorderBlurSlider':{
            'level': 1,
            'label': tr('Border Blur'),
            'min_value': '0',
            'max_value': '100',
            'default': '10',
            'step': 1,
            'help': tr('Border mask blending distance.')
        },
        'OccluderEnableToggle': {
            'level': 1,
            'label': tr('Occlusion Mask'),
            'default': False,
            'help': tr('Allow objects occluding the face to show up in the swapped image.')
        },
        'OccluderSizeSlider': {
            'level': 2,
            'label': tr('Size'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'OccluderEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Grows or shrinks the occluded region')
        },
        'DFLXSegEnableToggle': {
            'level': 1,
            'label': tr('DFL XSeg Mask'),
            'default': False,
            'help': tr('Allow objects occluding the face to show up in the swapped image.')
        },
        'DFLXSegSizeSlider': {
            'level': 2,
            'label': tr('Size'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'DFLXSegEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Grows or shrinks the occluded region.')
        },
        'OccluderXSegBlurSlider': {
            'level': 1,
            'label': tr('Occluder/DFL XSeg Blur'),
            'min_value': '0',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'OccluderEnableToggle | DFLXSegEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blend value for Occluder and XSeg.')
        },
        'ClipEnableToggle': {
            'level': 1,
            'label': tr('Text Masking'),
            'default': False,
            'help': tr('Use descriptions to identify objects that will be present in the final swapped image.')
        },
        'ClipText': {
            'level': 2,
            'label': tr('Text Masking Entry'),
            'min_value': '0',
            'max_value': '1000',
            'default': '',
            'width': 130,
            'parentToggle': 'ClipEnableToggle',
            'requiredToggleValue': True,
            'help': tr('To use, type a word(s) in the box separated by commas and press <enter>.')
        },
        'ClipAmountSlider': {
            'level': 2,
            'label': tr('Amount'),
            'min_value': '0',
            'max_value': '100',
            'default': '50',
            'step': 1,
            'parentToggle': 'ClipEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Increase to strengthen the effect.')
        },
        'FaceParserEnableToggle': {
            'level': 1,
            'label': tr('Face Parser Mask'),
            'default': False,
            'help': tr('Allow the unprocessed background from the orginal image to show in the final swap.')
        },
        'BackgroundParserSlider': {
            'level': 2,
            'label': tr('Background'),
            'min_value': '-50',
            'max_value': '50',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Negative/Positive values shrink and grow the mask.')
        },
        'FaceParserSlider': {
            'level': 2,
            'label': tr('Face'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the entire face.')
        },
        'LeftEyebrowParserSlider': {
            'level': 2,
            'label': tr('Left Eyebrow'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the left eyebrow.')
        },
        'RightEyebrowParserSlider': {
            'level': 2,
            'label': tr('Right Eyebrow'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the right eyebrow.')
        },
        'LeftEyeParserSlider': {
            'level': 2,
            'label': tr('Left Eye'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the left eye.')
        },
        'RightEyeParserSlider': {
            'level': 2,
            'label': tr('Right Eye'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the right eye.')
        },
        'EyeGlassesParserSlider': {
            'level': 2,
            'label': tr('EyeGlasses'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the eyeglasses.')
        },
        'NoseParserSlider': {
            'level': 2,
            'label': tr('Nose'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the nose.')
        },
        'MouthParserSlider': {
            'level': 2,
            'label': tr('Mouth'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the inside of the mouth, including the tongue.')
        },
        'UpperLipParserSlider': {
            'level': 2,
            'label': tr('Upper Lip'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the upper lip.')
        },
        'LowerLipParserSlider': {
            'level': 2,
            'label': tr('Lower Lip'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the lower lip.')
        },
        'NeckParserSlider': {
            'level': 2,
            'label': tr('Neck'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the neck.')
        },
        'HairParserSlider': {
            'level': 2,
            'label': tr('Hair'),
            'min_value': '0',
            'max_value': '30',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the size of the Mask. Mast the hair.')
        },
        'BackgroundBlurParserSlider': {
            'level': 2,
            'label': tr('Background Blur'),
            'min_value': '0',
            'max_value': '100',
            'default': '5',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blend the value for Background Parser')
        },
        'FaceBlurParserSlider': {
            'level': 2,
            'label': tr('Face Blur'),
            'min_value': '0',
            'max_value': '100',
            'default': '5',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blend the value for Face Parser')
        },
        'FaceParserHairMakeupEnableToggle': {
            'level': 2,
            'label': tr('Hair Makeup'),
            'default': False,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Enable hair makeup')
        },
        'FaceParserHairMakeupRedSlider': {
            'level': 3,
            'label': tr('Red'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle & FaceParserHairMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Red color adjustments')
        },
        'FaceParserHairMakeupGreenSlider': {
            'level': 3,
            'label': tr('Green'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 3,
            'parentToggle': 'FaceParserEnableToggle & FaceParserHairMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Green color adjustments')
        },
        'FaceParserHairMakeupBlueSlider': {
            'level': 3,
            'label': tr('Blue'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle & FaceParserHairMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blue color adjustments')
        },
        'FaceParserHairMakeupBlendAmountDecimalSlider': {
            'level': 3,
            'label': tr('Blend Amount'),
            'min_value': '0.1',
            'max_value': '1.0',
            'default': '0.2',
            'step': 0.1,
            'decimals': 1,
            'parentToggle': 'FaceParserEnableToggle & FaceParserHairMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blend the value: 0.0 represents the original color, 1.0 represents the full target color.')
        },
        'FaceParserLipsMakeupEnableToggle': {
            'level': 2,
            'label': tr('Lips Makeup'),
            'default': False,
            'parentToggle': 'FaceParserEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Enable lips makeup')
        },
        'FaceParserLipsMakeupRedSlider': {
            'level': 3,
            'label': tr('Red'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle & FaceParserLipsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Red color adjustments')
        },
        'FaceParserLipsMakeupGreenSlider': {
            'level': 3,
            'label': tr('Green'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 3,
            'parentToggle': 'FaceParserEnableToggle & FaceParserLipsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Green color adjustments')
        },
        'FaceParserLipsMakeupBlueSlider': {
            'level': 3,
            'label': tr('Blue'),
            'min_value': '0',
            'max_value': '255',
            'default': '0',
            'step': 1,
            'parentToggle': 'FaceParserEnableToggle & FaceParserLipsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blue color adjustments')
        },
        'FaceParserLipsMakeupBlendAmountDecimalSlider': {
            'level': 3,
            'label': tr('Blend Amount'),
            'min_value': '0.1',
            'max_value': '1.0',
            'default': '0.2',
            'step': 0.1,
            'decimals': 1,
            'parentToggle': 'FaceParserEnableToggle & FaceParserLipsMakeupEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blend the value: 0.0 represents the original color, 1.0 represents the full target color.')
        },
        'RestoreEyesEnableToggle': {
            'level': 1,
            'label': tr('Restore Eyes'),
            'default': False,
            'help': tr('Restore eyes from the original face.')
        },
        'RestoreEyesBlendAmountSlider': {
            'level': 2,
            'label': tr('Eyes Blend Amount'),
            'min_value': '1',
            'max_value': '100',
            'default': '50',
            'step': 1,
            'parentToggle': 'RestoreEyesEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Increase this to show more of the swapped eyes. Decrease it to show more of the original eyes.')
        },
        'RestoreEyesSizeFactorDecimalSlider': {
            'level': 2,
            'label': tr('Eyes Size Factor'),
            'min_value': '2.0',
            'max_value': '4.0',
            'default': '3.0',
            'decimals': 1,
            'step': 0.5,
            'parentToggle': 'RestoreEyesEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Reduce this when swapping faces zoomed out of the frame.')
        },
        'RestoreEyesFeatherBlendSlider': {
            'level': 2,
            'label': tr('Eyes Feather Blend'),
            'min_value': '1',
            'max_value': '100',
            'default': '10',
            'step': 1,
            'parentToggle': 'RestoreEyesEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the blending of eyes border. Increase this to show more of the original eyes. Decrease this to show more of the swapped eyes.')
        },
        'RestoreXEyesRadiusFactorDecimalSlider': {
            'level': 2,
            'label': tr('X Eyes Radius Factor'),
            'min_value': '0.3',
            'max_value': '3.0',
            'default': '1.0',
            'decimals': 1,
            'step': 0.1,
            'parentToggle': 'RestoreEyesEnableToggle',
            'requiredToggleValue': True,
            'help': tr('These parameters determine the shape of the mask. If both are equal to 1.0, the mask will be circular. If either one is greater or less than 1.0, the mask will become oval, stretching or shrinking along the corresponding direction.')
        },
        'RestoreYEyesRadiusFactorDecimalSlider': {
            'level': 2,
            'label': tr('Y Eyes Radius Factor'),
            'min_value': '0.3',
            'max_value': '3.0',
            'default': '1.0',
            'decimals': 1,
            'step': 0.1,
            'parentToggle': 'RestoreEyesEnableToggle',
            'requiredToggleValue': True,
            'help': tr('These parameters determine the shape of the mask. If both are equal to 1.0, the mask will be circular. If either one is greater or less than 1.0, the mask will become oval, stretching or shrinking along the corresponding direction.')
        },
        'RestoreXEyesOffsetSlider': {
            'level': 2,
            'label': tr('X Eyes Offset'),
            'min_value': '-300',
            'max_value': '300',
            'default': '0',
            'step': 1,
            'parentToggle': 'RestoreEyesEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Moves the Eyes Mask on the X Axis.')
        },
        'RestoreYEyesOffsetSlider': {
            'level': 2,
            'label': tr('Y Eyes Offset'),
            'min_value': '-300',
            'max_value': '300',
            'default': '0',
            'step': 1,
            'parentToggle': 'RestoreEyesEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Moves the Eyes Mask on the Y Axis.')
        },
        'RestoreEyesSpacingOffsetSlider': {
            'level': 2,
            'label': tr('Eyes Spacing Offset'),
            'min_value': '-200',
            'max_value': '200',
            'default': '0',
            'step': 1,
            'parentToggle': 'RestoreEyesEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Change the Eyes Spacing distance.')
        },
        'RestoreMouthEnableToggle': {
            'level': 1,
            'label': tr('Restore Mouth'),
            'default': False,
            'help': tr('Restore mouth from the original face.')
        },
        'RestoreMouthBlendAmountSlider': {
            'level': 2,
            'label': tr('Mouth Blend Amount'),
            'min_value': '1',
            'max_value': '100',
            'default': '50',
            'step': 1,
            'parentToggle': 'RestoreMouthEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Increase this to show more of the swapped Mouth. Decrease it to show more of the original Mouth.')
        },       
        'RestoreMouthSizeFactorSlider': {
            'level': 2,
            'label': tr('Mouth Size Factor'),
            'min_value': '5',
            'max_value': '60',
            'default': '25',
            'step': 5,
            'parentToggle': 'RestoreMouthEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Increase this when swapping faces zoomed out of the frame.')
        },
        'RestoreMouthFeatherBlendSlider': {
            'level': 2,
            'label': tr('Mouth Feather Blend'),
            'min_value': '1',
            'max_value': '100',
            'default': '10',
            'step': 1,
            'parentToggle': 'RestoreMouthEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the border of Mouth blending. Increase this to show more of the original Mouth. Decrease this to show more of the swapped Mouth.')
        },
        'RestoreXMouthRadiusFactorDecimalSlider': {
            'level': 2,
            'label': tr('X Mouth Radius Factor'),
            'min_value': '0.3',
            'max_value': '3.0',
            'default': '1.0',
            'decimals': 1,
            'step': 0.1,
            'parentToggle': 'RestoreMouthEnableToggle',
            'requiredToggleValue': True,
            'help': tr('These parameters determine the shape of the mask. If both are equal to 1.0, the mask will be circular. If either one is greater or less than 1.0, the mask will become oval, stretching or shrinking along the corresponding direction.')
        },
        'RestoreYMouthRadiusFactorDecimalSlider': {
            'level': 2,
            'label': tr('Y Mouth Radius Factor'),
            'min_value': '0.3',
            'max_value': '3.0',
            'default': '1.0',
            'decimals': 1,
            'step': 0.1,
            'parentToggle': 'RestoreMouthEnableToggle',
            'requiredToggleValue': True,
            'help': tr('These parameters determine the shape of the mask. If both are equal to 1.0, the mask will be circular. If either one is greater or less than 1.0, the mask will become oval, stretching or shrinking along the corresponding direction.')
        },
        'RestoreXMouthOffsetSlider': {
            'level': 2,
            'label': tr('X Mouth Offset'),
            'min_value': '-300',
            'max_value': '300',
            'default': '0',
            'step': 1,
            'parentToggle': 'RestoreMouthEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Moves the Mouth Mask on the X Axis.')
        },
        'RestoreYMouthOffsetSlider': {
            'level': 2,
            'label': tr('Y Mouth Offset'),
            'min_value': '-300',
            'max_value': '300',
            'default': '0',
            'step': 1,
            'parentToggle': 'RestoreMouthEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Moves the Mouth Mask on the Y Axis.')
        },
        'RestoreEyesMouthBlurSlider': {
            'level': 1,
            'label': tr('Eyes/Mouth Blur'),
            'min_value': '0',
            'max_value': '50',
            'default': '0',
            'step': 1,
            'parentToggle': 'RestoreEyesEnableToggle | RestoreMouthEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the blur of mask border.')
        },
    },
    
    tr('Face Color Correction'):{
        'AutoColorEnableToggle': {
            'level': 1,
            'label': tr('AutoColor Transfer'),
            'default': False,
            'help': tr('Enable AutoColor Transfer: 1. Hans Test without mask, 2. Hans Test with mask, 3. DFL Method without mask, 4. DFL Original Method.')
        },
        'AutoColorTransferTypeSelection':{
            'level': 2,
            'label': tr('Transfer Type'),
            'options': ['Test', 'Test_Mask', 'DFL_Test', 'DFL_Orig'],
            'default': 'Test',
            'parentToggle': 'AutoColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Select the AutoColor transfer method type. Hans Method could have some artefacts sometimes.')
        },
        'AutoColorBlendAmountSlider': {
            'level': 1,
            'label': tr('Blend Amount'),
            'min_value': '0',
            'max_value': '100',
            'default': '80',
            'step': 5,
            'parentToggle': 'AutoColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the blend value.')
        },
        'ColorEnableToggle': {
            'level': 1,
            'label': tr('Color Adjustments'),
            'default': False,
            'help': tr('Fine-tune the RGB color values of the swap.')
        },
        'ColorRedSlider': {
            'level': 1,
            'label': tr('Red'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'ColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Red color adjustments')
        },
        'ColorGreenSlider': {
            'level': 1,
            'label': tr('Green'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'ColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Green color adjustments')
        },
        'ColorBlueSlider': {
            'level': 1,
            'label': tr('Blue'),
            'min_value': '-100',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'parentToggle': 'ColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Blue color adjustments')
        },
        'ColorBrightnessDecimalSlider': {
            'level': 1,
            'label': tr('Brightness'),
            'min_value': '0.00',
            'max_value': '2.00',
            'default': '1.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'ColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the Brightness.')
        },
        'ColorContrastDecimalSlider': {
            'level': 1,
            'label': tr('Contrast'),
            'min_value': '0.00',
            'max_value': '2.00',
            'default': '1.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'ColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the Contrast.')
        },
        'ColorSaturationDecimalSlider': {
            'level': 1,
            'label': tr('Saturation'),
            'min_value': '0.00',
            'max_value': '2.00',
            'default': '1.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'ColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the Saturation.')
        },
        'ColorSharpnessDecimalSlider': {
            'level': 1,
            'label': tr('Sharpness'),
            'min_value': '0.0',
            'max_value': '2.0',
            'default': '1.0',
            'step': 0.1,
            'decimals': 1,
            'parentToggle': 'ColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the Sharpness.')
        },
        'ColorHueDecimalSlider': {
            'level': 1,
            'label': tr('Hue'),
            'min_value': '-0.50',
            'max_value': '0.50',
            'default': '0.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'ColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the Hue.')
        },
        'ColorGammaDecimalSlider': {
            'level': 1,
            'label': tr('Gamma'),
            'min_value': '0.00',
            'max_value': '2.00',
            'default': '1.00',
            'step': 0.01,
            'decimals': 2,
            'parentToggle': 'ColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Changes the Gamma.')
        },
        'ColorNoiseDecimalSlider': {
            'level': 1,
            'label': tr('Noise'),
            'min_value': '0.0',
            'max_value': '20.0',
            'default': '0.0',
            'step': 0.5,
            'decimals': 1,
            'parentToggle': 'ColorEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Add noise to swapped face.')
        },

        'JPEGCompressionEnableToggle': {
            'level': 1,
            'label': tr('JPEG Compression'),
            'default': False,
            'help': tr('Apply JPEG Compression to the swapped face to make output more realistic'),
        },
        'JPEGCompressionAmountSlider': {
            'level': 2,
            'label': tr('Compression'),
            'min_value': '1',
            'max_value': '100',
            'default': '50',
            'step': 1,
            'parentToggle': 'JPEGCompressionEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the JPEG Compression amount')
        }
    },
    tr('Blend Adjustments'):{
        'FinalBlendAdjEnableToggle': {
            'level': 1,
            'label': tr('Final Blend'),
            'default': False,
            'help': tr('Blend at the end of pipeline.')
        },
        'FinalBlendAmountSlider': {
            'level': 2,
            'label': tr('Final Blend Amount'),
            'min_value': '1',
            'max_value': '50',
            'default': '1',
            'step': 1,
            'parentToggle': 'FinalBlendAdjEnableToggle',
            'requiredToggleValue': True,
            'help': tr('Adjust the final blend value.')
        },
        'OverallMaskBlendAmountSlider': {
            'level': 1,
            'label': tr('Overall Mask Blend Amount'),
            'min_value': '0',
            'max_value': '100',
            'default': '0',
            'step': 1,
            'help': tr('Combined masks blending distance. It is not applied to the border masks.')
        },        
    },
}