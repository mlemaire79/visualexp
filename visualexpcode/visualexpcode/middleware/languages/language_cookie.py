from django.utils import translation

class LanguageCookieMiddleware():

    def process_request(self, request):
        """
        Sets language from the cookie value.
        """

        if request.COOKIES.get('site_language'):
            language = request.COOKIES['site_language']
            # You should add here some code to check teh language
            # variable is safe...
            translation.activate(language)
            request.LANGUAGE_CODE = translation.get_language()

    def process_response(self, request, response):
        """
        Create cookie if not there already.

        Also deactivates language.
        (See http://stackoverflow.com/a/13031239/388835 )
        """

        if not request.COOKIES.get('site_language'):
            response.set_cookie('site_language',
                                '')
        translation.deactivate()
        return response