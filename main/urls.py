from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import ajax_login, ajax_register, register
from main.views import login_user
from main.views import logout_user
from . import views
from main.views import edit_product
from main.views import delete_product
from main.views import add_product_entry_ajax
from main.views import show_main, get_products_in_json 

from main.views import (
    delete_product, show_main, create_product, show_product,
    show_xml, show_json, show_xml_by_id, show_json_by_id
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('get-products/', get_products_in_json, name='get_products_json'),
    path('add-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'), 
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('ajax-login/', ajax_login, name='ajax_login'),
    path('ajax-register/', ajax_register, name='ajax_register'),
]