from typing import List

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str):
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name: str):
        for p in self.products:
            if p.name == product_name:
                self.products.remove(p)

    def __repr__(self) -> str:
        return "\n".join(f"{p.name}: {p.quantity}" for p in self.products)
