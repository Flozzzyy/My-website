from django.shortcuts import render

def mainpage(request):
    data={
        'title':'Главная страница!!!',
        'values':['some','hello','123'],
        'obj': {
            'car': 'bmw',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)

def about_page(request):
    return render(request,'main/about.html')

def kontaks(request):
    return render(request, 'main/kontakt.html')