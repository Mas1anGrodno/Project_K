from django.utils.translation import gettext as _
from rest_framework.response import Response

class LanguageMixin:
    def get_language(self, request):
        return request.query_params.get('lang', 'en')


    # def translate_content(self, content, lang):
    #     from django.utils import translation
    #     translation.activate(lang)
    #     translated_content = {
    #         key: _(value) if isinstance(value, str) else value
    #         for key, value in content.items()
    #     }
    #     translation.deactivate()
    #     return translated_content
    
    def translate_content(self, content, lang):
        from django.utils import translation
        translation.activate(lang)
    
        def translate_item(item):
            if isinstance(item, dict):
                return {key: translate_item(value) for key, value in item.items()}
            elif isinstance(item, list):
                return [translate_item(element) for element in item]
            elif isinstance(item, str):
                return _(item)
            else:
                return item
        translated_content = translate_item(content)
        translation.deactivate()
        return translated_content

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        lang = self.get_language(request)
        translated_data = [self.translate_content(item, lang) for item in response.data]
        return Response(translated_data)
