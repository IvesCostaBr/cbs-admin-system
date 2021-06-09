class MetaData(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     if request.user.is_authenticated:
    #         message = 'Olá %s, Bem vindo' % request.user.username
    #     else:
    #         message = 'bem vindo'
            
    #     request.session['message'] = message
        
    #     return None
        