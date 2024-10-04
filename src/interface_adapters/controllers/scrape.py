import asyncio
from flask import Blueprint, request, jsonify
from src.infraestructure.scraper_service import ScraperService

bp = Blueprint('scrape', __name__)
scraper_service = ScraperService()


@bp.route('/')
def index():
    return "API is working!"


@bp.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    products = scraper_service.scrape_products(url)
    return jsonify({'url': url, 'products': products})
