class Product:
    def __init__(self, sku: str, name: str, description: str, price: float):
        self.sku: str = sku
        self.name: str = name
        self.description: str = description
        self.unit_price: float = price
