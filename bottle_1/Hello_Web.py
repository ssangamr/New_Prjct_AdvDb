from bottle import route, run, template

@route('/hello/<my_name>')
def get_hello(my_name):
    return template("Hello {{name}}!", name = my_name)

@route('/goodbye')
def get_goodbye():
    return "Goodbye there!"

run(host='localhost', port=8080)