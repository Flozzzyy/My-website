from django.conf import settings  
from django.conf.urls.static import static  
from django.urls import path, include  

urlpatterns = [  
    path('', include('main.urls')),  # Для маршрута главной страницы  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  