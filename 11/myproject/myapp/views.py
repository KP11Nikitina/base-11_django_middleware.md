from django.http import HttpResponse

def error_view(request):
    raise Exception("Это тестовое исключение") 