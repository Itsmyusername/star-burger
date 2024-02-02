import json 

from django.http import JsonResponse
from django.templatetags.static import static


from .models import Product, Order, OrderItem


def banners_list_api(request):
    # FIXME move data to db?
    return JsonResponse([
        {
            'title': 'Burger',
            'src': static('burger.jpg'),
            'text': 'Tasty Burger at your door step',
        },
        {
            'title': 'Spices',
            'src': static('food.jpg'),
            'text': 'All Cuisines',
        },
        {
            'title': 'New York',
            'src': static('tasty.jpg'),
            'text': 'Food is incomplete without a tasty dessert',
        }
    ], safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


def product_list_api(request):
    products = Product.objects.select_related('category').available()

    dumped_products = []
    for product in products:
        dumped_product = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'special_status': product.special_status,
            'description': product.description,
            'category': {
                'id': product.category.id,
                'name': product.category.name,
            } if product.category else None,
            'image': product.image.url,
            'restaurant': {
                'id': product.id,
                'name': product.name,
            }
        }
        dumped_products.append(dumped_product)
    return JsonResponse(dumped_products, safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


def register_order(request):
    try:
        data = json.loads(request.body.decode())
    except ValueError:
        return JsonResponse({
            'error': 'Invalid JSON data',
        })

    # Проверяем наличие поля "products" в данных заказа
    if 'products' in data:
        products_data = data['products']
        # Создаем новый заказ
        order = Order.objects.create(
            firstname=data.get('firstname', ''),
            lastname=data.get('lastname', ''),
            phonenumber=data.get('phonenumber', ''),
            address=data.get('address', ''),
            status=data.get('status', 'new'),
        )

        # Добавляем продукты в заказ
        for product_data in products_data:
            product_id = product_data['product']
            quantity = product_data['quantity']

            # Создайте запись о продукте для заказа
            OrderItem.objects.create(
                order=order,
                product_id=product_id,
                quantity=quantity,
            )

        return JsonResponse({
            'message': 'Order registered successfully',
            'data': data,  # You can include additional data in the response
        })
    else:
        return JsonResponse({
            'error': 'No products in the order data',
        })