from client_wrapper import client_wrapper

def main():
    wrapper = client_wrapper()

    while True:
        print("\n------ Menu ------")
        print("1. Listar usuários")
        print("2. Listar tarefas de um usuário")
        print("3. Criar usuário")
        print("4. Atualizar usuário")
        print("5. Deletar usuário")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuarios = wrapper.listar_usuarios()
            for usuario in usuarios:
                print(f"{usuario['id']}: {usuario['name']} ({usuario['username']}) - {usuario['email']}")
        
        elif opcao == "2":
            user_id = input("Digite o id do usuário: ")
            tarefas = wrapper.listar_tarefas_usuario(user_id)
            for tarefa in tarefas:
                status = "Concluida" if tarefa['completed'] else "Pendente"
                print(f"[{status}] {tarefa['title']}")
        
        elif opcao == "3":
            nome = input("Digite o nome: ")
            username = input("Digite o username: ")
            email = input("Digite o email: ")
            dados_usuario = {"name": nome, "username": username, "email": email}
            response = wrapper.criar_usuario(dados_usuario)
            if response.status_code == 201:
                print("Usuário criado", response.json())
            else:
                print("Erro ao criar usuário.")
        
        elif opcao == "4":
            user_id = input("Digite o id do usuário: ")
            nome = input("Digite o novo nome: ")
            username = input("Digite o novo username: ")
            email = input("Digite o novo email: ")
            dados_usuario = {"name": nome, "username": username, "email": email}
            response = wrapper.atualizar_usuario(user_id, dados_usuario)
            if response.status_code == 200:
                print("Usuário atualizado:", response.json())
            else:
                print("Erro ao atualizar usuário.")
        
        elif opcao == "5":
            # Deletar um usuário
            user_id = input("Digite o id do usuário: ")
            status_code = wrapper.deletar_usuario(user_id)
            if status_code == 200:
                print(f"Usuário com id {user_id} deletado com sucesso.")
            else:
                print("Erro ao deletar usuário.")
        
        elif opcao == "6":
            print("Encerrando...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
