from flask import Flask

app = Flask(__name__)
@app.route('/')
def page():
   return "Welcome to the Page"

@app.route('/root/')
def root():
   return "hello flask";

@app.route('/greet/<name>')

def greet(name):
   return "Hello %s" %name


if __name__ == '__main__':
   app.run()

