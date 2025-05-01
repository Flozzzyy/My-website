from django.shortcuts import render

def mainpage(request):
    return render(request, 'main/index.html')

def about_page(request):
    return render(request,'main/about.html')

