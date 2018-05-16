from django.http.response import JsonResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from .models import Category, Product
from .serializers import ProductSerializer


class CategoriesView(View):
    http_method_names = ['get']

    def get(self, request):
        categories = Category.objects.all()
        return JsonResponse({
            "categories": [category.name for category in categories]
        })


class CategoryView(View):
    http_method_names = ['get']

    def get(self, request, category_name):
        try:
            category = Category.objects.get(name=category_name)
        except ObjectDoesNotExist as e:
            return JsonResponse({
                "success": False,
                "message": "Category '{}' does not exist".format(category_name),
            })

        products = category.product_set.all()

        return JsonResponse({
            "products": [ProductSerializer(p).as_dict() for p in products],
        })


class ClickProductView(View):
    http_method_names = ['post']

    def post(self, request):
        try:
            product_id = request.POST['id']
        except KeyError:
            return JsonResponse({
                "success": False,
                "message": "Field 'id' is required."
            })

        try:
            product = Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Product with id {} wasn't found".format(product_id)
            })

        product.clicks += 1
        product.save()

        return JsonResponse({
            "success": True,
            "product": ProductSerializer(product).as_dict()
        })
