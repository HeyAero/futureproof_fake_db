import json
from controllers import people

class TestAPICase():
  def test_welcome(self, api):
    res = api.get('/')
    assert res.status == '200 OK'
    assert res.json['message'] == 'Hello from futureproof DB!'

  def test_get_people(self, api):
    res = api.get('/people')
    assert res.status == '200 OK'
    assert len(res.json) == 4

  def test_get_person(self, api):
    check_data = [1,"Beth","True"]
    res = api.get('/people/1')
    assert res.status == '200 OK'
    assert res.json[0] == check_data

  def test_get_person_error(self, api):
    res = api.get('/people/6')
    assert res.status == '400 BAD REQUEST'
    assert 'Bad request:' in res.json['message']

  def test_post_people(self, api):
    mock_data = json.dumps({'name': 'Billy', 'teacher': 'False'})
    mock_headers = {'Content-Type': 'application/json'}
    res = api.post('/people', data=mock_data, headers=mock_headers)
    assert res.json[0][0] == 5

  def test_not_found(self, api):
    res = api.get('/cool')
    assert res.status == '404 NOT FOUND'
    assert 'Could not be found:' in res.json['message']