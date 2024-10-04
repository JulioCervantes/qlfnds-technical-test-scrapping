class Product:
    def __init__(self, sku, allergens, vegan, kosher, organic, vegetarian, gluten_free,
                 lactose_free, package_quantity, unit_size, net_weight):
        self.sku = sku
        self.allergens = allergens
        self.vegan = vegan
        self.kosher = kosher
        self.organic = organic
        self.vegetarian = vegetarian
        self.gluten_free = gluten_free
        self.lactose_free = lactose_free
        self.package_quantity = package_quantity
        self.unit_size = unit_size
        self.net_weight = net_weight
