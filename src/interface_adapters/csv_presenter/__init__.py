import csv


class CsvPresenter:
    @staticmethod
    def save(products, filepath):
        fieldnames = ['allergens', 'sku', 'vegan', 'kosher', 'organic', 'vegetarian', 'gluten_free',
                      'lactose_free', 'package_quantity', 'unit_size', 'net_weight']
        with open(filepath, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for product in products:
                for key in fieldnames:
                    if key == 'allergens':
                        product.__dict__[key] = [item["name"] for item in product.__dict__[key]['value']]
                    else:
                        product.__dict__[key] = product.__dict__[key]['value']
                writer.writerow(product.__dict__)