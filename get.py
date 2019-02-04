from flask import Flask,request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login',methods=['POST','GET'])
def login():
    data = request.get_json()
    name = data['id']
    print(name)
    return name


if __name__ == '__main__':
    app.run(debug=True)