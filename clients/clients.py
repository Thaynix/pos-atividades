import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_user_input(prompt):
    return input(prompt)

def listar_usuarios():
    response = requests.get(f"{BASE_URL}/users")
    if response.ok:
        for usuario in response.json():
            print(f"{usuario['id']}: {usuario['name']} ({usuario['username']}) - {usuario['email']}")
    else:
        print("X erro ao tentar listar usuários X")

def listar_tarefas_usuario():
    user_id = get_user_input("digite o id do usuário: ")
    response = requests.get(f"{BASE_URL}/users/{user_id}/todos")
    if response.ok:
        for tarefa in response.json():
            print(f"[{'OK' if tarefa['completed'] else 'X'}] {tarefa['title']}")
    else:
        print("X erro ao listar tarefas X")

def criar_usuario():
    dados_usuario = {
        "name": get_user_input("Digite o nome: "),
        "username": get_user_input("Digite o username: "),
        "email": get_user_input("Digite o e-mail: ")
    }
    response = requests.post(f"{BASE_URL}/users", json=dados_usuario)
    print("usuário criado!!! :D" if response.status_code == 201 else "X erro ao criar usuário X", response.json())

def ver_usuario():
    user_id = get_user_input("digite o id do usuário: ")
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    print(response.json() if response.ok else "usuário não encontrado :C")

def atualizar_usuario():
    user_id = get_user_input("digite o id do usuário: ")
    dados_usuario = {
        "name": get_user_input("novo nome: "),
        "username": get_user_input("novo username: "),
        "email": get_user_input("novo e-mail: ")
    }
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=dados_usuario)
    print("Usuário atualizado!" if response.ok else "Erro ao atualizar usuário.", response.json())

def deletar_usuario():
    user_id = get_user_input("Digite o ID do usuário: ")
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    print("Usuário deletado!" if response.ok else "Erro ao deletar usuário.")

def main():
    menu = {
        "1": listar_usuarios,
        "2": listar_tarefas_usuario,
        "3": criar_usuario,
        "4": ver_usuario,
        "5": atualizar_usuario,
        "6": deletar_usuario
    }

    while True:
        escolha = get_user_input("\n1. Listar usuários\n2. Listar tarefas\n3. Criar usuário\n4. Ver usuário\n5. Atualizar usuário\n6. Deletar usuário\n7. Sair\nEscolha: ")
        if escolha == "7":
            print(":C Encerrando...")
            break
        menu.get(escolha, lambda: print("XXX opção errada XXX"))()

if __name__ == "__main__":
    main()
