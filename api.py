import json

from flask import make_response, abort, jsonify
from tinydb import TinyDB, Query, where
import re


def get_products(name=''):
    """
    Gets all the products from the database

    :param name: str to be used sa a filter for the query
    :return: list of products
    """
    db = TinyDB('db/ecommerce.json')
    tb_products = db.table('products')
    product = Query()
    if not name:
        products_resp = tb_products.all()
    else:
        products_resp = tb_products.search(product.name.search(f'{name}', flags=re.IGNORECASE))

    return jsonify(products_resp)


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


def delete_item(id):
    db = TinyDB('db/ecommerce.json')
    tb_cart = db.table('items')
    tb_cart.remove(doc_ids=[int(id)])
    return make_response(
        "Item deleted", 200
    )
