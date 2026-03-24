"""
Gabriel Miravite
March 24, 2026
Lab 15: RESTful APIs & Unit Test in a Flask App
"""

from flask import Flask, request, jsonify, render_template

app = Flask (__name__)

# in-memory database (dictionary)
items = {}

@app.route('/')
def home():
    return render_template('index.html')

# CREATE an item
@app.route('/items', methods =['POST'])
def create_item():
    # get_json method is used to read JSON data sent by the client in an HTTP request
    data = request.get_json()

    # generate a new unique ID for the new item
    item_id = str(len(items)+1)

    # add the data collected for the new item
    items[item_id] = data

    # jsonify converts a Python dictionary into a json response, and ret
    return jsonify({'id':item_id, 'item': data}), 201

# READ ALL ITEMS
@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(items)

# READ SINGLE ITEM
@app.route('/items/<item_id>', methods=['GET'])
def get_oneitem(item_id):
    item = items.get(item_id)
    if not item:
        # 404 = serve is reachable but the item you asked for doesn't exist
        return jsonify({'Error':"Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)