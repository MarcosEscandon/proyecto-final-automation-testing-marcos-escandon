import pytest
import requests
from utils.logger import get_logger

logger = get_logger()
BASE_URL = "https://jsonplaceholder.typicode.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

class TestJsonPlaceholderAPI:

    @pytest.mark.api
    def test_get_users_list(self):
        """Test GET /users para obtener lista de usuarios."""
        logger.info("Iniciando test_get_users_list")
        response = requests.get(f"{BASE_URL}/users", headers=HEADERS)
        
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        logger.info("GET /users verificado correctamente")

    @pytest.mark.api
    def test_create_user(self):
        """Test POST /users para crear un usuario."""
        logger.info("Iniciando test_create_user")
        payload = {
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz"
        }
        response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
        
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Leanne Graham"
        assert "id" in data
        logger.info(f"Usuario creado con ID: {data['id']}")

    @pytest.mark.api
    def test_delete_user(self):
        """Test DELETE /users/{id} para eliminar un usuario."""
        logger.info("Iniciando test_delete_user")
        user_id = 1
        response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
        
        assert response.status_code == 200
        logger.info(f"Usuario {user_id} eliminado correctamente")

    @pytest.mark.api
    def test_create_and_get_post_flow(self):
        """Test de flujo: Crear post y verificar."""
        logger.info("Iniciando test_create_and_get_post_flow")
        
        # 1. Crear Post
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        create_response = requests.post(f"{BASE_URL}/posts", json=payload, headers=HEADERS)
        assert create_response.status_code == 201
        post_id = create_response.json()["id"]
        logger.info(f"Post creado con ID: {post_id}")
        
        # 2. Verificar que podemos consultar un post existente (JSONPlaceholder no persiste nuevos)
        existing_id = 1
        get_response = requests.get(f"{BASE_URL}/posts/{existing_id}", headers=HEADERS)
        assert get_response.status_code == 200
        assert get_response.json()["id"] == existing_id
        logger.info("Flujo de creación y consulta finalizado")
