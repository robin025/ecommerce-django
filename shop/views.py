from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderInfo
from math import ceil
import json


# Create your views here.
def index(request):

    all_products = []
    divide_Categories = Product.objects.values('category')
    divided_Categories = {item['category'] for item in divide_Categories}
    for categories in divided_Categories:
        divided_products = Product.objects.filter(category=categories)
        n = len(divided_products)
        nos = n // 4 + ceil((n / 4) - (n // 4))
        all_products.append([divided_products, range(1, nos), nos])

    context = {'all_prods': all_products}
    print(all_products)
    return render(request, 'shop/index.html', context)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    thank = False
    if request.method == "POST":
        # print(request)
        name = request.POST.get('name', 'Error')
        # print(name)
        email = request.POST.get('email', 'Error')
        # print(email)
        phone = request.POST.get('phone', 'error')
        # print(phone)
        desc = request.POST.get('desc', '')
        # print(desc)
        contact_info = Contact(contact_name=name,
                               contact_email=email,
                               contact_phone=phone,
                               contact_desc=desc)
        contact_info.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})


def tracker(request):
    if request.method == "POST":
        track_id = request.POST.get('orderid', 'error')
        track_email = request.POST.get('email', 'Error')
        track_phone = request.POST.get('phone', 'error')

        try:
            order = Order.objects.filter(order_id=track_id,
                                         order_email=track_email,
                                         order_phone=track_phone)
            print(order)
            if len(order) > 0:
                track_update = OrderInfo.objects.filter(order_id=track_id)
                updates = []
                for item in track_update:
                    updates.append({
                        "text": item.order_desc,
                        "time": item.timestamp,
                    })
                    response = json.dumps(
                        [updates, order[0].items_json, order[0]], default=str)

                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def prodview(request, my_id):
    
    product_fetched = Product.objects.filter(
        id=my_id
    )  
    print(product_fetched)  
    context1 = {
        'product': product_fetched[0]
    }  
    return render(
        request, 'shop/prodview.html', context1
    )  


def checkOut(request):
    if request.method == "POST":

        name = request.POST.get('name', 'Error')
        items_JSON = request.POST.get('itemsjson', 'Error')

        email = request.POST.get('email', 'Error')

        phone = request.POST.get('phone', 'error')

        addres2 = request.POST.get('address1', '') + " " + request.POST.get(
            'address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_codes', '')

        order_info = Order(items_json=items_JSON,
                           order_name=name,
                           order_email=email,
                           order_phone=phone,
                           order_address=addres2,
                           city=city,
                           state=state,
                           zip_code=zip_code)

        order_info.save()
        update_order = OrderInfo(
            order_id=order_info.order_id,
            order_desc="Your Order Has Been Placed Succesfully")
        update_order.save()
        thank = True
        id_no = order_info.order_id  
        print(id_no)
        return render(request, 'shop/checkout.html', {
            'thank': thank,
            'id': id_no
        })
    return render(request, 'shop/checkout.html')
