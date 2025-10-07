from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import register
from main.views import login_user
from main.views import logout_user
from . import views
from main.views import edit_product
from main.views import delete_product
from main.views import add_product_entry_ajax
# main/urls.py
from django.urls import path
from main.views import show_json
 

app_name = 'main'

urlpatterns = [
    # ... URL lainnya
    # Perhatikan bagian name='...' di bawah ini
    path('json/', show_json, name='show_json'), 
]


from main.views import (
    delete_product, show_main, create_product, show_product,
    show_xml, show_json, show_xml_by_id, show_json_by_id
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('delete/<uuid:pk>/', views.delete_product, name="delete_product"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:Product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:Product_id>/', show_json_by_id, name='show_json_by_id'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit-product-ajax/<int:product_id>/', views.edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<int:product_id>/', views.delete_product_ajax, name='delete_product_ajax'),
    path('json/', show_json, name='show_json'),
     path('add-product-ajax/', views.add_product_ajax, name='add_product_ajax'),
]
