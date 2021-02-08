from flask import Flask, jsonify, request, render_template

# Create Flask object
app = Flask(__name__)


stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    },
    {
        'name': 'My Second Store',
        'items': [
            {
                'name': 'My second item',
                'price': 2.99
            }
        ]
    }
]


@app.route('/')
def home():
    return render_template('index.html')


# POST  - Used to receive data
# GET  - Used to send data back only

# POST /store data: {name:} Create store for a given name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name> Return a store for a given name
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores and return the one that matches
    # If not match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found.'})


# GET /store Return all stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item Create an item inside a store with a given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found.'})


# GET /store/<string:name>/item Return all items in an specific store
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'Store not found.'})


app.run(port=5000)
