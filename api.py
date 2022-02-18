from flask import make_response, jsonify
from tinydb import TinyDB, Query, where
import re

from api_interface import IEcommerceAPI


class ECommerceAPITinyDB(IEcommerceAPI):

    @staticmethod
    def get_products(name=''):
        db = TinyDB('db/ecommerce.json')
        tb_products = db.table('products')
        product = Query()
        if not name:
            products_resp = tb_products.all()
        else:
            products_resp = tb_products.search(product.name.search(f'{name}', flags=re.IGNORECASE))

        return jsonify(products_resp)

    @staticmethod
    def add_item_to_cart(item):
        if set(item.keys()).issubset(('productSku', "quantity")) and item['quantity'] > 0:
            db = TinyDB('db/ecommerce.json')
            tb_cart = db.table('items')
            item_id = tb_cart.insert(item)
            tb_products = db.table('products')
            product = tb_products.search(where('sku') == item['productSku'])
            new_item = {
                "id": item_id,
                "product": product,
                "quantity": item['quantity']
            }

            return jsonify(new_item)
        else:
            return make_response(
                "Missing Required Information", 400
            )

    @staticmethod
    def delete_item(item_id):
        db = TinyDB('db/ecommerce.json')
        tb_cart = db.table('items')
        tb_cart.remove(doc_ids=[int(item_id)])
        return make_response(
            "Item deleted", 200
        )
