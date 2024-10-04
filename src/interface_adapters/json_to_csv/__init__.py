from src.infraestructure.json_repository import JsonRepository
from src.interface_adapters.csv_presenter import CsvPresenter
from src.core.usecases.format_data import FormatData

JSON_DEFAULT_FILE = 'https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json'
CSV_DEFAULT_FILE = 'products.csv'


def json_to_csv(json_file, csv_file):
    if json_file is None:
        json_file = JSON_DEFAULT_FILE
    if csv_file is None:
        csv_file = CSV_DEFAULT_FILE
    json_repository = JsonRepository()
    csv_presenter = CsvPresenter()
    format_data = FormatData(json_repository, csv_presenter)
    format_data.execute(json_file, csv_file)
    print(f"Json file formatted to csv file {csv_file} successfully!")
