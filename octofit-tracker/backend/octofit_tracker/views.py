from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit API!",
        "url": "https://jubilant-adventure-5gqwjxv6rg4jcv44j-8000.app.github.dev"
    })
