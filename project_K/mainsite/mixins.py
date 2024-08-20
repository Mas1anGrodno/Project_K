
from deep_translator import GoogleTranslator
from rest_framework.response import Response

class TranslationMixin:
    def translate_text(self, text, dest_language):
        translator = GoogleTranslator(source='auto', target=dest_language)
        return translator.translate(text)

    def translate_response(self, data, dest_language):
        if isinstance(data, list):
            return [self.translate_response(item, dest_language) for item in data]
        elif isinstance(data, dict):
            return {key: self.translate_text(value, dest_language) if isinstance(value, str) else value for key, value in data.items()}
        return data

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        dest_language = request.query_params.get('lang', 'en')
        response.data = self.translate_response(response.data, dest_language)
        return response

