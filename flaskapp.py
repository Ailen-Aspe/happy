@app.route('./root')

def name():
    return 'hello flask'

@app.route('./greet/<name>')

def greet(name):
    name = raw_input("Username: ")
    return "hello %s" %name


name = input()
greet(name)