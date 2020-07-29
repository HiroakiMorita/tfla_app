from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<string:user_name>/<int:user_no>')
def show_user(user_name, user_no):
    user_name_no = user_name + str(user_no)
    return '<h1>{}</h1>'.format(user_name_no)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)