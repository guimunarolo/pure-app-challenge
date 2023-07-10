from rest_framework import status


def test_hello_world_response(client):
    response = client.get("/")

    assert response.status_code == status.HTTP_404_NOT_FOUND
