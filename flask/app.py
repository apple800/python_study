from flask import Flask

# Init app
app = Flask(__name__)

# URI, endpoint
@app.route('/', methods=['GET'])
def main():
    return '<h1> This is the main function</h1>'

if __name__ == '__main__':
    app.run(debug=True)