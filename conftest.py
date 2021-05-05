import pytest
import app
from controllers import people

@pytest.fixture
def api(monkeypatch):
  api = app.app.test_client()
  return api