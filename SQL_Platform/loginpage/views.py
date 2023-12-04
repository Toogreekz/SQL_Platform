from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as dlogin, logout as dlogout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from .models import *
from .query_parser import query_result


@login_required(login_url='login')
def homepage(request):
    return render(request, 'loginpage/lobby.html')


@login_required(login_url='login')
def rating(request):
    return render(request, 'loginpage/rating.html')


@login_required(login_url='login')
def task_page(request, n=1):
    task = Tasks.objects.get(pk=n)
    try:
        if task is not None and task.is_active:
            return render(request, 'loginpage/task_page.html', context={'task': task})
    except ObjectDoesNotExist: 
        return redirect(reverse('task', args=("1")))
    return redirect(reverse('task', args=("1")))


@csrf_exempt
def get_query_result(request):
    if request.method == "POST" and request.is_ajax():
        query = request.POST.get('query')
        task_id = request.POST.get('task_id')
        benchmark = Tasks.objects.get(pk=task_id)
        benchmark_query = benchmark.benchmark_query
        st1, result_benchmark = query_result(benchmark_query)
        st2, result = query_result(query)
        if st1 and st2:
        
            c = Solutions.objects.filter(Q(tasks_id=task_id) & Q(user_id=request.user.id) & Q(status=0))
            print(c)
            if not c and result == result_benchmark:
                user = User.objects.get(pk=request.user.id)
                print(user.tasks_completed)
                user.tasks_completed = user.tasks_completed + 1
                print(user.tasks_completed)
                user.save()
                
        a = Solutions()
        a.input = query
        if result == result_benchmark and st1 and st2:
            a.status = 0
        else:
            a.status = 1
        a.tasks_id = task_id
        a.user_id = request.user.id
        a.save()
        
        data = {'result': result,
                'result_benchmark': result_benchmark}
        return JsonResponse(data)
        

def login(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            dlogin(request, user)
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'loginpage/login_page.html')


def logout(request):
    dlogout(request)
    return HttpResponseRedirect(reverse('login'))


def stats_page(request):
    return render(request, 'loginpage/stats_page.html')
