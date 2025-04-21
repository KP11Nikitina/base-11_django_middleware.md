class SimpleLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Requested path: {request.path}")
        response = self.get_response(request)
        return response
class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Custom-Header'] = 'Привет, промежуточное ПО!'
        return response
    
    from django.core.cache import cache
from django.http import HttpResponseTooManyRequests
from time import time
from django.core.cache import cache 

class RateLimitingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        current_time = int(time())
        cache_key = f"{ip}:{current_time // 60}"

        requests_count = cache.get(cache_key, 0)

        if requests_count >= 10:
            return HttpResponseTooManyRequests("Слишком много запросов")

        cache.set(cache_key, requests_count + 1, timeout=60)
        response = self.get_response(request)

        return response 
    class ContentModificationMiddleware:
    
      def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if 'text/html' in response['Content-Type']:
            content = response.content.decode('utf-8')
            content = content.replace("Django", "Python Django")
            response.content = content.encode('utf-8')

        return response