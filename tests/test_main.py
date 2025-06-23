import sys
import os
from fastapi.testclient import TestClient
from app.main import app
import pytest
 
client = TestClient(app)
 
# Mock pour psycopg2
class MockCursor:
    def execute(self, query, params=None):
        if "SELECT" in query:
            self.results = [(1, "Alice", "Engineer")]
        elif "INSERT" in query:
            self.last_query = query
            self.last_params = params
 
    def fetchall(self):
        return self.results
 
    def close(self):
        pass
 
class MockConnection:
    def cursor(self):
        return MockCursor()
    def commit(self):
        pass
    def close(self):
        pass
 
@pytest.fixture
def mock_db(mocker):
    mocker.patch("app.main.get_connection", return_value=MockConnection())
 
def test_get_employees(mock_db):
    res = client.get("/employees")
    assert res.status_code == 200
    assert res.json() == [{"id": 1, "name": "Alice", "role": "Engineer"}]
 
def test_add_employee(mock_db):
    new_emp = {"id": 2, "name": "Bob", "role": "Manager"}
    res = client.post("/employees", json=new_emp)
    assert res.status_code == 200
    assert res.json() == new_emp

def test_root():
    assert True