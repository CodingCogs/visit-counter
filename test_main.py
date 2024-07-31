from fastapi.testclient import TestClient

from main import app, data_base

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"landing_visit": int(data_base.get("landing_visit"))}
    data_base.decr("landing_visit")
