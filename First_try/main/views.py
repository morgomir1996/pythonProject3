from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '322'],
        'obj': {
            'kind': 'amazon',
            'name': 'Kiesha',
            'age': 'ten'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
# Create your views here.
