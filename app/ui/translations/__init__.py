from PySide6.QtCore import QTranslator, QLocale
from PySide6.QtWidgets import QApplication
import os

class TranslationManager:
    def __init__(self):
        self.translators = {}
        self.current_language = "en"
        self.app = None
        
    def set_application(self, app: QApplication):
        self.app = app
        
    def load_translation(self, language: str) -> bool:
        if language not in self.translators:
            translator = QTranslator()
            translations_dir = os.path.join(os.path.dirname(__file__))
            
            if translator.load(f"{language}", translations_dir):
                self.translators[language] = translator
                return True
            return False
        return True
        
    def set_language(self, language: str) -> bool:
        if self.app is None:
            return False
            
        for translator in self.translators.values():
            self.app.removeTranslator(translator)
            
        if self.load_translation(language):
            self.current_language = language
            self.app.installTranslator(self.translators[language])
            return True
        return False

translation_manager = TranslationManager()

def setup_translations(app: QApplication):
    translation_manager.set_application(app)
    translation_manager.set_language("en") 