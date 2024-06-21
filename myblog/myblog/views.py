from django.shortcuts import redirect

def redirect_to_news(request):
    return redirect('/news/')
