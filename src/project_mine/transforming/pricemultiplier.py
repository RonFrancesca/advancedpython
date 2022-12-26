from src.project.transforming.transform import Transform
from src.project.product import Product
from src.project.utils import accepts_types

class PriceMultiplier(Transform):

    def __init__(self, multiplier: float) -> None:
        self.multiplier = multiplier

    @accepts_types(Product)
    def apply(self, product: Product) -> Product:
        """generate a new product with the price multiplied by self.multiplier

        Args:
            product (Product): product to transform

        Returns:
            Product: product transformed
        """
        return Product(name=product.name, 
                        currency=product.currency, 
                        price=product.price * self.multiplier)
        
