from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/books', methods=['GET'])
def get_all_books_v2():
    arr = ["book1", "book2"]
    return jsonify(arr)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
