from werkzeug.exceptions import BadRequest
import sqlite3
import app

def index(req):
  people = app.query_db('select * from people;')
  return people, 200

def create(req):
  new_person = req.get_json()
  query = 'insert into people (name, teacher) values (?, ?);'
  arguments = (new_person["name"], new_person["teacher"])
  return_value = app.query_db(query, arguments)
  print(return_value)
  return return_value, 201