from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .forms import UserForm, LoginPage
from .models import Person 
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import user_passes_test
from .models import Moshaver



def home(request):
    # بخوانید تمام ردیف‌های مدل Moshaver
    moshaver_list = Moshaver.objects.all()
    return render(request, 'home-2.html', {'moshaver_list': moshaver_list})



def about(request):
    return render(request, 'about-2.html')

def contact(request):
    return render(request, 'contact-2.html')

def footer(request):
    return render(request, 'footer.html')

def header(request):
    return render(request, 'header.html')

from django.shortcuts import render
from .models import Courses

def courses_list(request):
    courses_data = Courses.objects.all()
    return render(request, 'courses-list-7.html', {'courses_data': courses_data})

def coursesSingle(request):
    return render(request, 'courses-single-1.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def dshbAdmin(request):
    return render(request, 'dshb-administration.html')

from django.contrib.auth import authenticate, login
from .models import Person  # اگر مدل Person در همان فایل قرار دارد

from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse
from .models import Person  # جایگزین کنید با مسیر مدل واقعی شما

from django.shortcuts import render, HttpResponse, redirect
from .models import Person
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginPage(request.POST)        
        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    
                    login(request, user)
                    return redirect('home')
                
                else:
                    messages.error(request, 'حساب شما غیرفعال است.')
            else:
                print('user is None')
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
        else:
            print(form.errors)
            messages.error(request, 'لطفاً اطلاعات را به درستی وارد کنید.')
    else:
        form = LoginPage()
    
    return render(request, 'login.html', {'form': form})



def shopOrder(request):
    return render(request, 'shop-order.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.password = make_password(form.password)
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            if Person.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, 'Username is already taken. Please choose a different one.')
                return render(request, 'signup.html', {'form': form})
            new_user.save()
            login(request, new_user)
            messages.success(request, 'User created successfully.')
            return redirect('register_done')
        else:
            messages.error(request, 'Cannot save new user.')
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def shopCart(request):
    cart = request.session.get('cart', [])
    total_price = sum(item['price'] for item in cart)

    context = {
        'cart': cart,
        'total_price': total_price,
    }
    return render(request, 'shop-cart.html', context)


def shopCheckout(request):
    return render(request, 'shop-checkout.html')

def register(request):
    return render(request, 'shop-checkout.html')

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # form.password = make_password(form.password)
            form.save()
            return redirect('home')
        
    else:
        form = UserForm()
    
    return render(request, 'register.html', {'form': form})







from django.shortcuts import get_object_or_404, redirect
from .models import Courses

def add_to_cart(request, course_id):
   cart = cart(request)
   cart.add(course_id)


def remove_from_cart(request, course_id):
    cart = request.session.get('cart', [])
    cart = [item for item in cart if item['course_id'] != course_id]
    request.session['cart'] = cart
    return redirect('shopCart')  # یا هر جای دیگری که می‌خواهید ریدایرکت شود


