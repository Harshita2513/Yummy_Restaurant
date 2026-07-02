from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart/<int:id>/',views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove, name='remove')
    # path('', views.chefs, name='Chefs')
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
