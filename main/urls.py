from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import register
from main.views import login_user
from main.views import logout_user
from . import views

from main.views import (
    delete_product, show_main, create_product, show_product,
    show_xml, show_json, show_xml_by_id, show_json_by_id
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path("delete/<uuid:pk>/", views.delete_product, name="delete_product"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:Product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:Product_id>/', show_json_by_id, name='show_json_by_id'),
]

# Tambahkan ini untuk serve media files saat DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)