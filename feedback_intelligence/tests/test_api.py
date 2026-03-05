def test_analyze_endpoint(client):

    response = client.get("/analyze")

    assert response.status_code == 200
    assert "trend" in response.json()