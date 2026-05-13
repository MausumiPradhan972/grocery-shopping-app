import json
from django.shortcuts import render,redirect
from marts.models import Signin_model,contact_model,Product,Order,OrderItem
from django.http import JsonResponse
from collections import Counter
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def home(request):
    return render (request,'home.html')
def category(request):
    return render (request,'category.html')
def about(request):
    return render (request,'About-us.html')
def contact(request):
    print(request.method)
    print(request.POST)
    print(request.GET)
    if request.method=="POST":
        cName=request.POST.get("contactname")
        cEmail=request.POST.get("contactemail")
        cSub=request.POST.get("contactsubject")
        cmsg=request.POST.get("contactmessage")
        if cName and cEmail and cSub and cmsg:
           message=contact_model(name=cName,email=cEmail,sub=cSub,message=cmsg)
           message.save()
    return render (request,'contact-us.html')
    
def dairy(request):
    products=Product.objects.filter(category='dairy')
    return render (request,'dairy-bakery.html',{'products':products})
def cooking(request):
    products=Product.objects.filter(category='cooking')
    return render (request,'cooking.html',{'products':products})
def fruit(request):
    products=Product.objects.filter(category='fruit')
    return render (request,'fruit-vegetable.html',{'products':products})
def packaged(request):
    print("hello")
    print(Product)
    products=Product.objects.filter(category='packaged')
    return render (request,'packaged.html',{'products':products})
def signin(request):
    if request.session.get('globalValue'):
        return redirect('home')
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        person=Signin_model(name=name,email=email,password=password)
        person.save()
        request.session['user_id']=person.id
        return redirect('home')
    return render (request,'signin.html')
def user(request):
    user_id=request.session.get('user_id')
    print(user_id)
    print(request.session.items())
    if not user_id:
        return redirect('signin')
    user=Signin_model.objects.filter(id=user_id).first()
    return render (request,'user.html',{'myuser':user})
def detail(request):
    return render (request,'detail.html')
def cart(request):
    print("view hit")
    products=Product.objects.all()
    cart=request.session.get('cart',[])
    request.session['cart']=cart
    return render(request,"cart.html",{'products':products})

def signout(request):
    # request.session.flush()
    return render(request,'user.html')
def cart_page(request):
    cart=request.session.get('cart',[])
    print("cart page",request.session.get("cart"))
    from marts.models import Product
    products=request.GET.get('name')
    print("cart",cart,type(cart))
    return render(request,'cart.html',{
        'products':products
    })
def get_cart_products(request):
    import json
    body=request.body.decode("utf-8")
    print("body",body)
    if not body:
        return JsonResponse({
            "products":[]
        })
    data=json.loads(request.body)
    cart_data=data.get('cart',{})
    print("cart items",cart_data)
    print(cart_data)
    print(type(cart_data))
    product_ids=[]
    for item in cart_data:
        if item is None:
            continue
        if isinstance(item,int):
            product_id=item
            qty=1
        else:
           product_id=int(item["id"])
           qty=int(item['quantity'])
           product_ids.append(product_id)
        print("product id ",product_id,"quantity",qty)
    print("product ids",product_ids)
    products=Product.objects.filter(id__in=product_ids)
    product_list=[]
    for p in products:
        product_list.append({
            "id":p.id,
            "name":p.name,
            "price":p.price,
            "image":p.image.url,
        })
    print("product lit",product_list)
    return JsonResponse({
        'products':product_list
        })
def get_wishlist_products(request):
    import json
    data=json.loads(request.body)
    wishlist_ids=data.get('wishlist',[])
    print("cart ids",wishlist_ids)
    products=Product.objects.filter(id__in=wishlist_ids)
    product_list=[]
    for p in products:
        product_list.append({
            "id":p.id,
            "name":p.name,
            "price":str(p.price),
            "image":p.image.url,
        })
    return JsonResponse({'products':product_list})
def wishlist(request):
    return render(request,'wishlist.html')
# Create your views here.
def create_order(request):
    print("order view called")
    if request.method == "POST":
        data=json.loads(request.body)
        cart_list=data.get('cart',[])
        print("raw cart",cart_list)
        if not cart_list:
            return JsonResponse({"error":"cart empty"},status=400)
        cart=Counter(cart_list)
        print("convered cart",cart)
        order=Order.objects.create(total_price=0)
        
        total=0
        for product_id,qty in cart.items():
            try:
                product=Product.objects.get(id=product_id)
                print("productid",product_id,"qty",qty)
                print("adding",product.name)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=qty,
                    price=product.price
                )
                total+=float(product.price)*int(qty)
            except Product.DoesNotExist:
                continue
        order.total_price=total
        order.save()
        return JsonResponse({
            "message":"order created",
            "order_id":order.id
        })
    return JsonResponse({"error":"invalid reques"},status=400)
