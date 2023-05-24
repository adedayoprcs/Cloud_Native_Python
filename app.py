from flask import Flask, make_response, jsonify, request

app = Flask(__name__) 

books = { "1" :{
        "book_id": "1",
        "name": "A Game of Thrones.",
        "author": "George R. R. Martin"}} 

@app.route('/api/books', methods=['GET', 'POST'])
def get_books():
    if request.method == 'GET':
        return make_response(jsonify(books), 200)
    elif request.method == 'POST':
        content = request.json
        book_id = content['book_id']

        books[book_id] = content

        book_obj = books.get(book_id, {})
        return make_response(jsonify(book_obj, 201))
       


         

#@app.route("/")
#def index():
    #return "Hello World!"

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5000, debug=True)