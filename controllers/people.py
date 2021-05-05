from werkzeug.exceptions import BadRequest
import sqlite3
import app

def index(req):
  people = app.query_db('select * from people;')
  return people, 200

def create(req):
  new_person = req.get_json()

  return_value = app.query_db('insert into people (name, teacher) values (?, ?);', (new_person["name"], new_person["teacher"]))

  check_value = app.query_db('select id from people where name = (?);', (new_person["name"],))

  return check_value, 201