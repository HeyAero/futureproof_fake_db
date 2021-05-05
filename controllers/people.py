from werkzeug.exceptions import BadRequest

mock_people = [
  { 'id': 1, 'name': 'Beth', 'teacher': True },
  { 'id': 2, 'name': 'Aaron', 'teacher': False },
  { 'id': 3, 'name': 'Adil', 'teacher': False },
  { 'id': 4, 'name': 'Roselyn', 'teacher': False }
]

def index(req):
  return [p for p in mock_people], 200

def create(req):
  new_person = req.get_json()
  new_person['id'] = sorted([p['id'] for p in mock_people])[-1] + 1
  mock_people.append(new_person)
  return new_person, 201