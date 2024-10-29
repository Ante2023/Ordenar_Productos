from flask import Blueprint, request, jsonify
from .service import sort_products as sort_products_service #.service "." Indicamos que el módulo mismo directorio
sort_products_blueprint = Blueprint('sort_products', __name__)#__name__: Identifica módulo actual "controller"
@sort_products_blueprint.route('/sort-products', methods=['POST'])
def sort_products_endpoint():
    data = request.get_json()
    
    sales_weight = data['salesWeight']
    stock_weight = data['stockWeight']
    product_sales = data['productSales']
    product_stock = data['productStock']
    
    try:
        sorted_product_ids = sort_products_service(sales_weight, stock_weight, product_sales, product_stock)
        return jsonify(sorted_product_ids), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400
