from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
arr = ["book1"];

# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/books', methods=['GET'])
def get_all_books_v2():
    return jsonify(arr)


# API to add a book to the database
@app.route('/api/add_book', methods=['POST'])
def add_book():
    print("adding book")
    data = request.get_json()
    title = data.get('title')
    arr.append(title);
    return jsonify({'message': 'Book added successfully'})
 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
