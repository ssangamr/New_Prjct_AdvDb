import os
from bottle import get, post, template, request, redirect

ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ


#assert ON_PYTHONANYWHERE == True
if ON_PYTHONANYWHERE:
    from bottle import default_app
else:
    from bottle import  run, debug

from postgres_storage import get_items, get_item, update_status, create_item, update_item, delete_item


@get('/')
def get_show_list():
    result = get_items()
    return template("show_list", rows=result)

@get("/set_status/<id:int>/<value:int>")
def get_set_status(id,value):
    update_status(id,value)
    redirect("/")

@get("/new_item")
def get_new_item():
    return template("new_item")

@post("/new_item")
def post_new_item():
    new_item = request.forms.get("new_item").strip()
    create_item(new_item, 1)
    redirect("/")

@post("/new_item1")
def post_new_item():
    new_item = request.forms.get("new_item").strip()
    create_item(new_item, 1)
    redirect("/")

@post("/new_item2")
def post_new_item():
    new_item = request.forms.get("new_item").strip()
    create_item(new_item, 1)
    redirect("/")


@get("/update_item/<id:int>")
def get_update_item(id):
    result = get_item(id)
    return template("update_item", row=result)

@post("/update_item")
def post_update_item():
    id = int(request.forms.get("id").strip())
    updated_item = request.forms.get("updated_item").strip()
    update_item(id, updated_item)
    redirect("/")

@post("/update_item2")
def post_update_item():
    id = int(request.forms.get("id").strip())
    updated_item = request.forms.get("updated_item").strip()

@get("/delete_item/<id:int>")
def get_delete_item(id):
    delete_item(id)
    redirect("/")


if ON_PYTHONANYWHERE:
    application = default_app()
else:
    debug(True)
    run(host='localhost', port=8080)

