import requests

def test_get_google_homepage():
    response = requests.get("https://www.google.com")
    assert response.status_code == 200
    assert "Google" in response.text
