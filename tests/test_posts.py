import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    """Получение списка постов"""
    response = requests.get(f"{BASE_URL}/posts")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 100  # в сервисе ровно 100 постов

def test_get_post_by_id():
    """Получение одного поста по ID"""
    response = requests.get(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

def test_create_post():
    """Создание поста"""
    payload = {
        "title": "Test",
        "body": "Test body",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test"
    assert data["id"] == 101  # сервис всегда даёт ID 101 для новых

def test_update_post():
    """Обновление поста"""
    payload = {
        "id": 1,
        "title": "Updated"
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated"

def test_delete_post():
    """Удаление поста"""
    response = requests.delete(f"{BASE_URL}/posts/1")
    
    assert response.status_code == 200