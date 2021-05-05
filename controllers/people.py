from werkzeug.exceptions import BadRequest
import sqlite3
import app

def index(req):
  people = app.query_db('select * from people')
  return people, 200

def create(req):
  new_person = req.get_json()
  new_person['id'] = sorted([p['id'] for p in mock_people])[-1] + 1
  mock_people.append(new_person)
  return new_person, 201