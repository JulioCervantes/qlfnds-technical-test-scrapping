from src.core.entities.product import Product
import json

LOCALE_CODE = "es-CR"


class FormatData:
    def __init__(self, json_repository, csv_presenter):
        self.json_repository = json_repository
        self.csv_presenter = csv_presenter

    def execute(self, json_file, csv_file):
        json_raw = self.json_repository.load_json(json_file)
        product_data = json.loads(self.find_attribute(json_raw)[LOCALE_CODE])

        product = Product(
            sku=product_data['sku'],
            allergens=product_data['allergens'],
            vegan=product_data['vegan'],
            kosher=product_data['kosher'],
            organic=product_data['organic'],
            vegetarian=product_data['vegetarian'],
            gluten_free=product_data['gluten_free'],
            lactose_free=product_data['lactose_free'],
            package_quantity=product_data['package_quantity'],
            unit_size=product_data['unit_size'],
            net_weight=product_data['net_weight']
        )

        self.csv_presenter.save([product], csv_file)

    @staticmethod
    def find_attribute(json_raw,name="custom_attributes"):
        attributes = json_raw['allVariants'][0]['attributesRaw']
        for attribute in attributes:
            if attribute['name'] == name:
                return attribute['value']
        return None
