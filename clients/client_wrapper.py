import requests

class client_wrapper:
    api_url = "https://jsonplaceholder.typicode.com"

    def listar_usuarios(self):
        response = requests.get(f"{self.api_url}/users")
        return response.json()

    def listar_tarefas_usuario(self, user_id):
        response = requests.get(f"{self.api_url}/users/{user_id}/todos")
        return response.json()

    def criar_usuario(self, dados_usuario):
        response = requests.post(f"{self.api_url}/users", json=dados_usuario)
        return response
    
    def atualizar_usuario(self, user_id, dados_usuario):
        response = requests.put(f"{self.api_url}/users/{user_id}", json=dados_usuario)
        return response

    def deletar_usuario(self, user_id):
        response = requests.delete(f"{self.api_url}/users/{user_id}")
        return response.status_code