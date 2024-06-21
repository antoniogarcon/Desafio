"""
Método tem como função adicionar um contato na lista
"""
def adicionarContato(contatos, nome="", telefone="", email="", favorito=False):
    f = True if favorito =="Y" or favorito == "y" else False
    contatos.append({"nome":nome, "telefone":telefone, "email":email, "favorito":f})
    print(f"O contato {nome} foi adicionado coom sucesso!")
    return

"""
Método tem como função listar os contatos da lista
"""
def listarContatos(contatos):
    print("\nLista Contatos")
    for indice, contato in enumerate(contatos, start=1):
        print(f"{indice}. Nome: {contato["nome"]}, Telefone: {contato["telefone"]}, Email: {contato["email"]}, favorito: {contato["favorito"]}")
    return

"""
Método tem como função atualizar um contato
"""
def atualizarContato(contatos, indice, nome="", telefone="", email="", favorito=False):
    if indice >=0 and indice <= len(contatos):
        f = True if favorito =="Y" or favorito == "y" else False
        contatos[indice-1]["nome"] = nome
        contatos[indice-1]["telefone"] = telefone
        contatos[indice-1]["email"] = email
        contatos[indice-1]["favorito"] = f
        print(f"O contato {nome} foi atualizado com sucesso!")
    else:
        print(f"O indice {indice} é inválido!")
    return

"""
Método tem como função favoritar um contato
"""
def favoritarContato(contatos, indice):
    if indice >=0 and indice <= len(contatos):
        contatos[indice-1]["favorito"] = True
        print(f"O contato {contatos[indice-1]["nome"]} foi Favoritado!")
    else:
        print(f"O indice {indice} é inválido!")
    return

"""
Método tem como função favoritar um contato
"""
def listarContatosFavoritos(contatos):
    print("\nLista Contatos Favoritos")
    for indice, contato in enumerate(contatos,start=1):
        if contato["favorito"] :
            print(f"{indice}. Nome: {contato["nome"]}, Telefone: {contato["telefone"]}, Email: {contato["email"]}, favorito: {contato["favorito"]}")
    return

"""
Método tem como função remover um contato dos favoritos
"""
def desfavoritarContato(contatos, indice):
    if indice >=0 and indice <= len(contatos):
        contatos[indice-1]["favorito"] = False
        print(f"O contato {contatos[indice-1]["nome"]} foi removido dos favoritos!")
    else:
        print(f"O indice {indice} é inválido!")
    return

"""
Método tem como função remover um contato da lista
"""
def removerContato(contatos, indice):
    if indice >=0 and indice <= len(contatos):        
        contatos[indice-1]["favorito"] = False
        print(f"O contato {contatos[indice-1]["nome"]} foi removido dos favoritos!")
        contatos.remove(contatos[indice-1])
    else:
        print(f"O indice {indice} é inválido!")
    return

"""
Método tem como função listar o menu de opções do desafio
"""
def menu():
    
    print("\nMenu do gerenciador de CONTATOS")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Atualizar Contato")
    print("4. Favoritar Contato")
    print("5. Remover Contato dos Favoritos")
    print("6. Listar Contatos Favoritos")
    print("7. Deletar Contato")
    print("8. Sair")
    
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        nome = input("Qual o nome do contato? ")
        telefone = input("Qual o telefone do contato? ")
        email = input("Qual o email do contato? ")
        favorito = input("Contato Favorito (Y | N) :")
        adicionarContato(contatos, nome, telefone, email, favorito) 
        return True
    elif escolha == 2:
        listarContatos(contatos)
        return True
    elif escolha == 3:
        listarContatos(contatos)
        indice = int(input("Qual Contato você quer atualizar?? "))
        nome = input("Qual o nome do contato? ")
        telefone = input("Qual o telefone do contato? ")
        email = input("Qual o email do contato? ")
        favorito = input("Contato Favotiro (Y | N) :")
        atualizarContato(contatos, indice, nome, telefone, email, favorito)
        return True
    elif escolha == 4:
        listarContatos(contatos)
        indice = int(input("Qual Contato quer favoritar?? "))
        favoritarContato(contatos, indice)
        return True
    elif escolha == 5:
        listarContatos(contatos)
        indice = int(input("Qual Contato quer remover dos favoritos?? "))
        desfavoritarContato(contatos, indice)
        return True
    elif escolha == 6:
        listarContatosFavoritos(contatos)
        return True
    elif escolha == 7:
        listarContatos(contatos)
        indice = int(input("Qual Contato quer remover?? "))
        removerContato(contatos, indice)
        return True
    else:
        print("FIM!!!")
        return False

"""
- O contato pode ter os dados:
- Nome
- Telefone
- Email
- Favorito
"""
contatos = []
escolha = True

while escolha:
    menu()
