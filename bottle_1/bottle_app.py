import os
import sqlite3
from bottle import get, post, template, request, redirect

ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ


#assert ON_PYTHONANYWHERE == False
if ON_PYTHONANYWHERE:
    from bottle import default_app
else:
    from bottle import  run, debug



@get('/')
def get_show_list():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return template("show_list", rows=result)

@get("/new_item")
def get_new_item():
    return template("new_item")

@post("/new_item")
def post_new_item():
    new_item = request.forms.get("new_item").strip()
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("insert into todo (task, status) values(?,?)", (new_item,1))
    #cursor.lastrowid
    connection.commit()
    cursor.close()
    #return "The new item is [" + new_item + "]..."
    redirect("/")

if ON_PYTHONANYWHERE:
    application = default_app()
else:
    debug(True)
    run(host='localhost', port=8080)


    def():
    print("this is for test")
    def():
    print("this is for test2")
    def():
    print("this is for test3")
    def():
    print("this is for test4")

