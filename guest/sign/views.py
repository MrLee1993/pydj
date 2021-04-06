from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

#登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == '123':
            response = HttpResponseRedirect('/event_manage/')
            request.session['user']=username
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})
    else:
        return render(request, 'index.html', {'error': 'username or password error!'})

@login_required
def event_manage(request):
    username = request.session.get('user', '')  # 读取浏览器 cookie
    return render(request, "event_manage.html", {"user": username})