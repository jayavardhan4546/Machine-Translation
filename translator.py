from googletrans import Translator

class translation:

    def __init__(self, text, to_lang):
        self.text = text
        self.to_lang = to_lang

    def translate_word(self):
        translator = Translator()
        translated = translator.translate(self.text, src='en', dest=self.to_lang)
        return translated.text
