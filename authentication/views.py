from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags

from main.models import Product


# Create your views here.
@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Login status successful.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login successful!"
                # Add other data if you want to send data to Flutter.
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

@csrf_exempt
def logout(request):
    """
    Logout function for Flutter
    """
    username = request.user.username if request.user.is_authenticated else "Guest"
    
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout successful!"
        }, status=200)
    except Exception as e:
        return JsonResponse({
            "status": False,
            "message": f"Logout failed: {str(e)}"
        }, status=500)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']

        # Check if the passwords match
        if password1 != password2:
            return JsonResponse({
                "status": False,
                "message": "Passwords do not match."
            }, status=400)
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": False,
                "message": "Username already exists."
            }, status=400)
        
        # Create the new user
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        
        return JsonResponse({
            "username": user.username,
            "status": 'success',
            "message": "User created successfully!"
        }, status=200)
    
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = strip_tags(data.get("name", ""))
            price = data.get("price", 0)
            description = strip_tags(data.get("description", ""))
            category = data.get("category", "miscellaneous")
            thumbnail = data.get("thumbnail", "")
            user = request.user
            
            # Validasi user sudah login
            if not user.is_authenticated:
                return JsonResponse({
                    "status": "error",
                    "message": "User not authenticated"
                }, status=401)
            
            # Validasi nama tidak kosong
            if not name or len(name.strip()) < 2:
                return JsonResponse({
                    "status": "error",
                    "message": "Product name must be at least 2 characters"
                }, status=400)
            
            # Validasi price
            try:
                price = float(price)
                if price < 0:
                    return JsonResponse({
                        "status": "error",
                        "message": "Price cannot be negative"
                    }, status=400)
            except (ValueError, TypeError):
                return JsonResponse({
                    "status": "error",
                    "message": "Invalid price format"
                }, status=400)
            
            # Validasi description tidak kosong
            if not description or len(description.strip()) == 0:
                return JsonResponse({
                    "status": "error",
                    "message": "Product description cannot be empty"
                }, status=400)
            
            new_product = Product(
                name=name, 
                price=price,
                description=description,
                category=category,
                thumbnail=thumbnail,
                user=user
            )
            new_product.save()
            
            return JsonResponse({
                "status": "success",
                "message": "Product created successfully"
            }, status=200)
            
        except json.JSONDecodeError:
            return JsonResponse({
                "status": "error",
                "message": "Invalid JSON format"
            }, status=400)
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": f"Error: {str(e)}"
            }, status=500)
    else:
        return JsonResponse({
            "status": "error",
            "message": "Invalid request method"
        }, status=405)

# FUNGSI BARU: Menampilkan produk milik user yang login
@csrf_exempt
def show_my_products_json(request):
    """
    Mengembalikan produk yang dibuat oleh user yang sedang login
    """
    # Cek apakah user sudah login
    if not request.user.is_authenticated:
        return JsonResponse({
            'error': 'User not authenticated'
        }, status=401)
    
    # Filter produk berdasarkan user yang sedang login
    products = Product.objects.filter(user=request.user)
    
    # Serialisasi data
    data = []
    for product in products:
        data.append({
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'price': product.price,
            'date_added': product.date_added.isoformat(),
            'user': product.user.username,
            'user_id': product.user.id,
        })
    
    return JsonResponse(data, safe=False)