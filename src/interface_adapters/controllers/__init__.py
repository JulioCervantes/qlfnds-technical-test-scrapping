from flask import Flask
from src.interface_adapters.controllers.scrape import bp as scrape_bp


def run_api():
    app = Flask(__name__)
    app.register_blueprint(scrape_bp)
    app.run(host="0.0.0.0", port=5000)
