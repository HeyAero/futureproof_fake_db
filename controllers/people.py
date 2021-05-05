from werkzeug.exceptions import BadRequest
import sqlite3
import app

def index(req):
  people = app.query_db('select * from people;')
  return people, 200

def show(req, uid):
  fetch_result = find_by_uid(uid)
  if fetch_result == []:
    raise BadRequest(f"We don't have a person with that ID of {uid}")
  else:
    return fetch_result, 200

def create(req):
  new_person = req.get_json()
  return_value = app.query_db('insert into people (name, teacher) values (?, ?);', (new_person["name"], new_person["teacher"]))
  check_value = app.query_db('select id from people where name = (?);', (new_person["name"],))
  return check_value, 201

def find_by_uid(uid):
  try:
    return app.query_db('select * from people where id = (?);', (uid,))
  except:
    raise BadRequest(f"We don't have a person with that ID of {uid}")