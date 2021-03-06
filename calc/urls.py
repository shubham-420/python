from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('add', views.add, name = 'add'),
    path('accounts/', include('accounts.urls'))
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
