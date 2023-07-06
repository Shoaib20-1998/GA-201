from flask import Flask, request

app = Flask(__name__)

menu = [
    {'id': 1, 'name': 'Pizza', 'price': 15, 'availability': True},
    {'id': 2, 'name': 'Burger', 'price': 7, 'availability': True},
    {'id': 3, 'name': 'Pasta', 'price': 4, 'availability': False}
]

@app.route('/create', methods=['GET', 'POST'])
def create_item():
    if request.method == 'POST':
        data=request.get_json()
        menu.append(data)
        return "Item created successfully!"
    else:
        return '''
        <form method="POST">
            <label for="id">ID:</label>
            <input type="number" name="id" required><br><br>
            <label for="name">Name:</label>
            <input type="text" name="name" required><br><br>
            <label for="price">Price:</label>
            <input type="number" step="0.01" name="price" required><br><br>
            <label for="availability">Availability:</label>
            <input type="checkbox" name="availability"><br><br>
            <input type="submit" value="Create">
        </form>
        '''

@app.route('/read')
def read_items():
    output = ''
    for item in menu:
        output += f"ID: {item['id']}, Name: {item['name']}, Price: {item['price']}, Availability: {item['availability']}<br>"
    return output

@app.route('/update/<int:dish_id>', methods=["PATCH"])
def update_item(dish_id):
    if request.method == 'PATCH':
        data=request.get_json()
        item_id = int(dish_id)
        for item in menu:
            if item['id'] == item_id:
                item['name'] = data["name"]
                item['price'] = data["price"]
                item['availability'] = data["availability"]
                return "Item updated successfully!"
        return "Item not found!"
    else:
        return '''
        <form method="POST">
            <label for="id">ID:</label>
            <input type="number" name="id" required><br><br>
            <label for="name">Name:</label>
I apologize for the incomplete response. Here's the continuation of the code:

```python
            <input type="text" name="name" required><br><br>
            <label for="price">Price:</label>
            <input type="number" step="0.01" name="price" required><br><br>
            <label for="availability">Availability:</label>
            <input type="checkbox" name="availability"><br><br>
            <input type="submit" value="Update">
        </form>
        '''

@app.route('/delete/<int:dish_id>', methods=["DELETE"])
def delete_item(dish_id):
    if request.method == 'DELETE':
        item_id = int(dish_id)
        for item in menu:
            if item['id'] == item_id:
                menu.remove(item)
                return "Item deleted successfully!"
        return "Item not found!"
    else:
        return '''
        <form method="POST">
            <label for="id">ID:</label>
            <input type="number" name="id" required><br><br>
            <input type="submit" value="Delete">
        </form>
        '''

if __name__ == '__main__':
    app.run()