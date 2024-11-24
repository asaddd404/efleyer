# views.py
from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import *
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.decorators import  login_required

from django.contrib.auth.models import auth 
from  django.contrib.auth import authenticate,login,logout




def index(request):
    greeting = ("Hello, World!")
    sliders = Fashion.objects.all()
    sliders2 = Electronic.objects.all()
    sliders3=Accessories.objects.all()
    start=Start.objects.all()
    return render(request, 'index.html',
        {'sliders': sliders,
        'sliders2': sliders2, 
        'sliders3':sliders3,
        'start':start,
        'greeting': greeting})

def electronic(request):
    start=Start.objects.all()
    sliders2 = Electronic.objects.all()

    return render(request,'electronic.html',
        {'start':start,
        'sliders2': sliders2, 


        })

def fashion(request):
    start=Start.objects.all()
    sliders=Fashion.objects.all()    
    return render(request,'fashion.html',
        {'start':start,
        'sliders': sliders,
        })

def jewellery(request):
    start=Start.objects.all()
    sliders3=Accessories.objects.all()

    return render(request,'jewellery.html',
        {'start':start,
        'sliders3':sliders3,
  
        })
def secces(request): 
    return render(request,'secces.html',{})


def korzina(request): 
    return render(request,'korzina.html',{})


def register(request):
    form=UserForm()
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secces')
    return render(request,'register.html',{'form':form})


def login(request):
    form=LoginForm(request,data=request.POST)
    
    if form.is_valid():
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)



        if user is not None:
            auth.login(request,user)
            return redirect('secces')
    context={'form':form}

    return render(request,'login.html',context=context)

def logout_view(request): 
    logout(request)
    return redirect('login')



# Добавление товара в корзину
@login_required
def add_to_cart(request, product_id, model_name):
    if not product_id or not model_name:
        return redirect('cart_detail')

    # Определяем модель продукта в зависимости от model_name
    if model_name == "fashion":
        product = get_object_or_404(SliderContent, id=product_id)
        model_class = SliderContent
    elif model_name == "electronic":
        product = get_object_or_404(SliderContent2, id=product_id)
        model_class = SliderContent2
    elif model_name == "accessories":
        product = get_object_or_404(SliderContent3, id=product_id)
        model_class = SliderContent3
    else:
        return redirect('cart_detail')  # Если модель не указана или неверная, редиректим обратно

    # Получаем или создаем корзину пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Создаем или получаем CartItem для конкретного продукта
    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=ContentType.objects.get_for_model(model_class),
        object_id=product.id
    )

    # Если товар уже есть в корзине, увеличиваем количество
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')


# Отображение корзины
@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total_price = sum(item.get_total_price() for item in cart.items.all())
    
    return render(request, 'cart_detail.html', {
        'cart': cart,
        'total_price': total_price
    })


# Увеличение количества товара в корзине
@login_required
def increase_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')


# Уменьшение количества товара в корзине
@login_required
def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart_detail')


# Удаление товара из корзины
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')
