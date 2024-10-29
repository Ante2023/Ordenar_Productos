from flask import Flask
from app.controller import sort_products_blueprint

app = Flask(__name__)
app.register_blueprint(sort_products_blueprint)
if __name__ == '__main__':
    app.run(debug=True,  host='127.0.0.1', port=8080)