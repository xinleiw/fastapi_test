def test_hello(client):
    resp = client.get(url="/api/hello")
    assert resp.status_code == 200
    assert resp.json() == "Hello world"
