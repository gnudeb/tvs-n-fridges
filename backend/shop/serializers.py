from .models import Product


class ProductSerializer:
    def __init__(self, product: Product):
        self.product = product

    def as_dict(self):
        return {
            "id": self.product.id,
            "name": self.product.name,
            "category": self.product.category.name,
            "clicks": self.product.clicks,
        }
