
from django.shortcuts import redirect

class LogAndRestrictMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Petición a: {request.path} - Usuario: {request.user}")
        if request.path.startswith('/biblioteca/crear/') and not request.user.is_authenticated:
            return redirect('/admin/login/?next=' + request.path)
        response = self.get_response(request)
        return response
