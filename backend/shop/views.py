import json

from django.http.response import JsonResponse
from django.views.generic import View, TemplateView
from django.core.exceptions import ObjectDoesNotExist

from .models import Category, Product
from .serializers import ProductSerializer


class JsonPostView(View):
    """Abstract view that handles POST request with JSON payload."""
    http_method_names = ['post']
    required_fields = []

    def post(self, request):
        try:
            json_payload = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            })

        for field in self.required_fields:
            if field not in json_payload:
                return JsonResponse({
                    "success": False,
                    "message": "Expected field '{}'.".format(field)
                })

        return self.handle(request, json_payload)

    def handle(self, request, json_payload):
        raise NotImplementedError()


class SPAView(TemplateView):
    template_name = "spa.html"


class CategoriesView(View):
    http_method_names = ['get']

    def get(self, request):
        categories = Category.objects.all()
        return JsonResponse({
            "success": True,
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
            "success": True,
            "products": [ProductSerializer(p).as_dict() for p in products],
        })


class ProductView(View):
    http_method_names = ['get']

    def get(self, request, _id):
        try:
            product = Product.objects.get(id=_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Product with id {} wasn't found".format(_id)
            })

        return JsonResponse({
            "success": True,
            "product": ProductSerializer(product).as_dict()
        })


class ClickProductView(JsonPostView):
    required_fields = ['id']

    def handle(self, request, json_payload):
        try:
            product = Product.objects.get(id=json_payload['id'])
        except ObjectDoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Product with id {} wasn't found".format(json_payload['id'])
            })

        product.clicks += 1
        product.save()

        return JsonResponse({
            "success": True,
            "product": ProductSerializer(product).as_dict()
        })