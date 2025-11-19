<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, JsonResponse
=======

from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
>>>>>>> e242ebdab6d2ca6e2f599f6a27ba66733df14649
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
<<<<<<< HEAD
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):
=======
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

>>>>>>> e242ebdab6d2ca6e2f599f6a27ba66733df14649
    product_list = Product.objects.all()
    context = {
        'name': request.user.username,
        'class': 'PBP F',
<<<<<<< HEAD
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
=======
        'product_list': product_list, 
        'last_login': request.COOKIES.get('last_login', 'Never')

>>>>>>> e242ebdab6d2ca6e2f599f6a27ba66733df14649
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
<<<<<<< HEAD
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        messages.success(request, f"Produk '{product_entry.name}' berhasil ditambahkan!")
        return redirect('main:show_main')
    context = {'form': form}
=======

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }
>>>>>>> e242ebdab6d2ca6e2f599f6a27ba66733df14649
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()
<<<<<<< HEAD
    context = {'product': product}
    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'views': product.views,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'price': product.price,
            'user_id': product.user.id if product.user else None,
            'user_username': product.user.username if product.user else None,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, Product_id):
    try:
        product_list = Product.objects.filter(pk=Product_id)
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
       
        data = {
            "pk": product.pk,
            "fields": {
                "name": product.name,
                "description": product.description,
                "category": product.category,
                "thumbnail": product.thumbnail,
                "stock": product.stock,
                "price": product.price,
                "created_at": product.created_at,
                "is_featured": product.is_featured,
                "user": product.user.pk,
                "user_username": product.user.username, 
            }
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Not found"}, status=404)

def register(request):
    form = UserCreationForm()
=======
    context = {
        'product': product
    }
 
    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'title': product.title,
            'content': product.content,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def show_xml_by_id(request, Product_id):
   try:
       product_list = Product.objects.filter(pk=Product_id)
       xml_data = serializers.serialize("xml", product_list)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   

def show_json_by_id(request, Product_id):
   try:
       product_list = Product.objects.get(pk=Product_id)
       json_data = serializers.serialize("json", [product_list])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   

def register(request):
    form = UserCreationForm()

>>>>>>> e242ebdab6d2ca6e2f599f6a27ba66733df14649
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
<<<<<<< HEAD
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
=======
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
>>>>>>> e242ebdab6d2ca6e2f599f6a27ba66733df14649
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
<<<<<<< HEAD
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
=======

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
>>>>>>> e242ebdab6d2ca6e2f599f6a27ba66733df14649

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

<<<<<<< HEAD
=======
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('main:show_main')
>>>>>>> e242ebdab6d2ca6e2f599f6a27ba66733df14649

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
<<<<<<< HEAD
    name = strip_tags(request.POST.get("name"))
    price = int(request.POST.get("price") or 0)
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    stock = int(request.POST.get("stock") or 0)
    is_featured = request.POST.get("is_featured") in ['on', 'true', '1']
    user = request.user if request.user.is_authenticated else None

    product_product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        stock=stock,
        is_featured=is_featured,
        user=user
    )
    product_product.save()
    return HttpResponse(b"CREATED", status=201)

def get_products_in_json(request):
    products = Product.objects.all()
    return HttpResponse(serializers.serialize('json', products), content_type="application/json")

@csrf_exempt
def ajax_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "Invalid credentials"}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def ajax_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return JsonResponse({"success": False, "error": "Passwords do not match"}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "error": "Username already exists"}, status=400)
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid method"}, status=405)

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        
        # TAMBAHKAN PESAN SUKSES DI SINI
        messages.success(request, f"Product '{product.name}' has been updated successfully!")
        
        return redirect('main:show_main')
        
    context = {'form': form, 'product': product}
    return render(request, "edit_product.html", context)


@require_POST
@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    product_name = product.name # Simpan nama sebelum dihapus
    product.delete()

    messages.success(request, f"Product '{product_name}' has been deleted.")

    return redirect('main:show_main')

@csrf_exempt
def login(request):
    """
    API endpoint for user login from Flutter app.
    Expects POST data with username and password.
    """
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=405)

    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '')

    if not username or not password:
        return JsonResponse({
            "status": False,
            "message": "Username and password are required."
        }, status=400)

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login successful!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account is disabled."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, please check your username or password."
        }, status=401)
    
def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    """
    API endpoint for creating a product from Flutter app.
    Expects JSON payload with product details.
    """
    # if request.method != 'POST':
    #     return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

    # Check if user is authenticated
    if not request.user.is_authenticated:
        return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)

    # Extract and validate required fields
    name = strip_tags(data.get("title", "").strip())  # Map 'title' to 'name'
    description = strip_tags(data.get("description", "").strip())  # Map 'description' to 'description'
    category = data.get("category", "").strip()
    thumbnail = data.get("thumbnail", "").strip()
    price = data.get("price")
    stock = data.get("stock", 0)
    is_featured = data.get("is_featured", False)

    # Validation
    errors = []
    if not name:
        errors.append("Name is required")
    if not description:
        errors.append("Description is required")
    if not category:
        errors.append("Category is required")
    if price is None or not isinstance(price, (int, float)) or price < 0:
        errors.append("Valid price is required")
    if not isinstance(stock, int) or stock < 0:
        errors.append("Valid stock quantity is required")
    if category not in dict(Product.CATEGORY_CHOICES):
        errors.append("Invalid category")

    if errors:
        return JsonResponse({"status": "error", "message": "; ".join(errors)}, status=400)

    try:
        # Create product instance
        product = Product(
            name=name,
            description=description,
            category=category,
            thumbnail=thumbnail if thumbnail else None,
            price=int(price),
            stock=stock,
            is_featured=bool(is_featured),
            user=request.user
        )
        product.save()
        return JsonResponse({"status": "success", "product_id": str(product.id)}, status=201)
    except Exception as e:
        # Log the error for debugging
        return JsonResponse({"status": "error", "message": "Failed to create product"}, status=500)
=======
    title = request.POST.get("title")
    content = request.POST.get("content")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        title=title, 
        content=content,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    title = strip_tags(request.POST.get("title")) # strip HTML tags!
    content = strip_tags(request.POST.get("content")) # strip HTML tags!

@csrf_exempt 
def edit_product_ajax(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'GET':
        # Mengirim data produk yang ada untuk diisi ke form
        data = {
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
        }
        return JsonResponse(data)

    elif request.method == 'POST':
        # Menyimpan perubahan dari form
        product.name = strip_tags(request.POST.get("name"))
        product.price = request.POST.get("price")
        product.description = strip_tags(request.POST.get("description"))
        product.category = request.POST.get("category")
        product.thumbnail = request.POST.get("thumbnail")
        product.save()
        return JsonResponse({'status': 'success'}, status=200)
    
@csrf_exempt
def delete_product_ajax(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return JsonResponse({'status': 'success'}, status=200)
>>>>>>> e242ebdab6d2ca6e2f599f6a27ba66733df14649
