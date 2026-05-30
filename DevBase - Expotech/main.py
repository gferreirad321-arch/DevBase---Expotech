from conexao import conectar, fechar_conexao

# =========================================================
# SISTEMA DEVBASE - TERMINAL CRUD
# =========================================================


# ========================= USUÁRIO =========================
# Função: criar novo usuário no sistema
def criar_usuario():

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== CRIAR USUÁRIO ===")

        nome_usuario = input("Nome: ")
        email_usuario = input("Email: ")
        senha_usuario = input("Senha: ")
        sexo_usuario = input("Sexo (masculino/feminino ou vazio): ") or None

        query = """
            INSERT INTO tbl_usuario (nome_usuario, email_usuario, senha_usuario, sexo_usuario)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (nome_usuario, email_usuario, senha_usuario, sexo_usuario))
        conexao.commit()

        print("Agora vocë faz parte da DevBase!")

    except Exception as erro:
        print(f"Erro ao criar usuário. Tente novamente: {erro}")

    finally:
        if conexao:
            fechar_conexao(conexao)


# ========================= USUÁRIO =========================
# Função: autenticar login do usuário
def autenticar_usuario():

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== LOGIN ===")

        email_usuario = input("Email: ")
        senha_usuario = input("Senha: ")

        query = """
            SELECT * FROM tbl_usuario
            WHERE email_usuario = %s AND senha_usuario = %s
        """

        cursor.execute(query, (email_usuario, senha_usuario))
        usuario = cursor.fetchone()

        if usuario:
            print(f"Bem-vindo a DevBase desenvolvedor! {usuario[1]}!")
            return True
        else:
            print("Email ou senha incorretos!")
            return False

    except Exception as erro:
        print(f"Erro ao autenticar usuário. Tente novamente: {erro}")
        return False

    finally:
        if conexao:
            fechar_conexao(conexao)


# ========================= USUÁRIO =========================
# Função: listar todos os usuários
def listar_usuarios():

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== LISTA DE USUÁRIOS ===")

        query = """
                SELECT * FROM tbl_usuario
                """

        cursor.execute(query)
        lista_usuarios = cursor.fetchall()

        for usuario in lista_usuarios:
            print(f"""
ID: {usuario[0]}
Nome: {usuario[1]}
Email: {usuario[2]}
Sexo: {usuario[8]}
-----------------------
""")

    except Exception as erro:
        print(f"Erro ao listar usuários. Tente novamente: {erro}")

    finally:
        if conexao:
            fechar_conexao(conexao)


# ========================= USUÁRIO =========================
# Função: buscar usuário por ID
def buscar_usuario():

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== BUSCAR USUÁRIO ===")

        id_usuario = input("ID do usuário: ")

        query = """
            SELECT * FROM tbl_usuario
            WHERE id_usuario = %s
        """

        cursor.execute(query, (id_usuario,))
        usuario = cursor.fetchone()

        if usuario:
            print(f"""
ID: {usuario[0]}
Nome: {usuario[1]}
Email: {usuario[2]}
Sexo: {usuario[8]}
Data criação: {usuario[4]}
""")
        else:
            print("Usuário não encontrado")

    except Exception as erro:
        print(f"Erro ao buscar usuário. Tente novamente: {erro}")

    finally:
        if conexao:
            fechar_conexao(conexao)


# ========================= USUÁRIO =========================
# Função: atualizar dados do usuário
def atualizar_usuario():

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== ATUALIZAR USUÁRIO ===")

        id_usuario = input("ID do usuário: ")
        nome_usuario = input("Novo nome: ")
        email_usuario = input("Novo email: ")
        senha_usuario = input("Nova senha: ")
        sexo_usuario = input("Sexo: ") or None

        query = """
            UPDATE tbl_usuario
            SET nome_usuario=%s, email_usuario=%s, senha_usuario=%s, sexo_usuario=%s
            WHERE id_usuario=%s
        """

        cursor.execute(query, (nome_usuario, email_usuario, senha_usuario, sexo_usuario, id_usuario))
        conexao.commit()

        print("Usuário da DevBase atualizado!")

    except Exception as erro:
        print(f"Erro ao atualizar usuário. Tente novamente: {erro}")

    finally:
        if conexao:
            fechar_conexao(conexao)



# ========================= TÓPICO =========================
# Função: criar tópico no sistema
def criar_topico():

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== CRIAR TÓPICO ===")

        titulo_topico = input("Título: ")
        tipo_topico = input("Tipo: ")
        id_usuario = input("ID usuário: ")

        query = """
            INSERT INTO tbl_topico (titulo_topico, tipo_topico, id_usuario)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (titulo_topico, tipo_topico, id_usuario))
        conexao.commit()

        print("Tópico criado! Esse tópico é ótimo.")

    except Exception as erro:
        print(f"Erro ao criar tópico. Tente novamente: {erro}")

    finally:
        if conexao:
            fechar_conexao(conexao)


# ========================= TÓPICO =========================
# Função: listar tópicos
def listar_topicos():

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== LISTA DE TÓPICOS ===")

        query = """
                SELECT * FROM tbl_topico
                """

        cursor.execute(query)
        lista_topicos = cursor.fetchall()

        for topico in lista_topicos:
            print(f"""
ID: {topico[0]}
Título: {topico[1]}
Tipo: {topico[3]}
Usuário: {topico[4]}
-----------------------
""")

    except Exception as erro:
        print(f"Erro ao listar tópicos. Tente novamente: {erro}")

    finally:
        if conexao:
            fechar_conexao(conexao)


# ========================= CRIAR PERFIL =========================
    # Função: criar perfil do usuário
def criar_perfil():

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== CRIAR PERFIL ===")

        bio = input("Bio: ")
        nivel = input("Nível (iniciante/intermediario/avancado): ")
        area = input("Área de interesse: ")
        id_user = input("ID usuário: ")

        query = """
            INSERT INTO tbl_perfil (bio_perfil, nivel_perfil, area_interesse_perfil, id_usuario)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (bio, nivel, area, id_user))
        conexao.commit()

        print("Perfil criado!")

    except Exception as e:
        print(f"Erro ao criar perfil. Tente novamente: {e}")

    finally:
        fechar_conexao(conexao)


#========================= COMENTÁRIO =========================#
# Função: criar comentário
def criar_comentario():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== CRIAR COMENTÁRIO ===")

        texto = input("Comentário: ")
        id_usuario = input("ID usuário: ")
        id_topico = input("ID tópico: ")

        query = """
            INSERT INTO tbl_comentario (texto_comentario, id_usuario, id_topico)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (texto, id_usuario, id_topico))
        conexao.commit()

        fechar_conexao(conexao)
        print("Comentário criado!")

    except Exception as erro:
        print(f"Erro ao criar comentário. Tente novamente: {erro}")


#========================= CURTIDA =========================#
#Função: dar curtida
def curtir():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== CURTIR ===")

        id_usuario = input("ID usuário: ")
        tipo = input("Curtir (topico/comentario): ")

        if tipo == "topico":
            id_topico = input("ID tópico: ")
            id_comentario = None
        else:
            id_topico = None
            id_comentario = input("ID comentário: ")

        query = """
            INSERT INTO tbl_curtida (id_usuario, id_topico, id_comentario)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (id_usuario, id_topico, id_comentario))
        conexao.commit()

        fechar_conexao(conexao)
        print("Curtida registrada!")

    except Exception as erro:
        print(f"Erro para dar curtida. Tente novamente: {erro}")


#========================= FEEDBACK =========================#
# Função: realizar feedback
def enviar_feedback():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== FEEDBACK ===")

        msg = input("Mensagem: ")
        id_usuario = input("ID usuário: ")

        query = """
            INSERT INTO tbl_feedback (msg_feedback, id_usuario)
            VALUES (%s, %s)
        """

        cursor.execute(query, (msg, id_usuario))
        conexao.commit()

        fechar_conexao(conexao)
        print("Feedback enviado! Obrigado pelo feedback.")

    except Exception as erro:
        print(f"Erro para realizar feedback. Tente novamente: {erro}")


#========================= NOTIFICAÇÃO =========================#
# Função: criar notifi
def criar_notificacao():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== NOTIFICAÇÃO ===")

        msg = input("Mensagem: ")
        id_usuario = input("ID usuário: ")

        query = """
            INSERT INTO tbl_notificacao (msg_notificacao, id_usuario)
            VALUES (%s, %s)
        """

        cursor.execute(query, (msg, id_usuario))
        conexao.commit()

        fechar_conexao(conexao)
        print("Notificação criada!")

    except Exception as erro:
        print(f"Erro ao criar notificação. Tente novamente: {erro}")


#========================= ACESSO DIÁRIO =========================#
# Função: acesso diario
def registrar_acesso():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== ACESSO DIÁRIO ===")

        pontos = input("Pontos do dia: ")
        id_usuario = input("ID usuário: ")

        query = """
            INSERT INTO tbl_acesso_diario (pontuacao_dia_acesso_diario, id_usuario)
            VALUES (%s, %s)
        """

        cursor.execute(query, (pontos, id_usuario))
        conexao.commit()

        fechar_conexao(conexao)
        print("Acesso registrado! Volte sempre.")

    except Exception as erro:
        print(f"Erro ao registrar acesso. Tente novamente: {erro}")


#========================= PROJETO =========================#
# Função: criar projeto
def criar_projeto():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== PROJETO ===")

        titulo = input("Título: ")
        descricao = input("Descrição: ")
        link = input("Link: ") or None
        id_usuario = input("ID usuário: ")

        query = """
            INSERT INTO tbl_projeto (titulo_projeto, descricao_projeto, link_projeto, id_usuario)
            VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (titulo, descricao, link, id_usuario))
        conexao.commit()

        fechar_conexao(conexao)
        print("Projeto criado! Esse é um projeto grandioso.")

    except Exception as erro:
        print(f"Erro para criar projeto. Tente novamente: {erro}")


#========================= RECUPERAÇÃO DE SENHA =========================#
# Função: recuperar a senha
def gerar_recuperacao_senha():
    try:
        import uuid

        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== RECUPERAÇÃO DE SENHA ===")

        id_usuario = input("ID usuário: ")
        token = str(uuid.uuid4())

        query = """
            INSERT INTO tbl_recuperacao_senha (token_recuperacao_senha, id_usuario)
            VALUES (%s, %s)
        """

        cursor.execute(query, (token, id_usuario))
        conexao.commit()

        fechar_conexao(conexao)

        print("Token de senha gerado:", token)

    except Exception as erro:
        print(f"Erro para recuperação. Tente novamente: {erro}")


 # ========================= USUÁRIO =========================
# Função: deletar usuário (CASCADE manual depois)
def deletar_usuario():

    conexao = None

    try:
        conexao = conectar()
        cursor = conexao.cursor()

        print("\n=== DELETAR USUÁRIO ===")

        id_usuario = input("ID para deletar: ")

        # apaga dependências primeiro
        cursor.execute("DELETE FROM tbl_comentario WHERE id_usuario=%s", (id_usuario,))
        cursor.execute("DELETE FROM tbl_topico WHERE id_usuario=%s", (id_usuario,))
        cursor.execute("DELETE FROM tbl_perfil WHERE id_usuario=%s", (id_usuario,))
        cursor.execute("DELETE FROM tbl_feedback WHERE id_usuario=%s", (id_usuario,))
        cursor.execute("DELETE FROM tbl_notificacao WHERE id_usuario=%s", (id_usuario,))
        cursor.execute("DELETE FROM tbl_usuario WHERE id_usuario=%s", (id_usuario,))

        conexao.commit()

        print("Usuário deletado! Não há mais nenhum dado desse usuário em nosso sistema.")

    except Exception as erro:
        print(f"Erro ao deletar usuário. Tente novamente: {erro}")

    finally:
        if conexao:
            fechar_conexao(conexao)


# ========================= MENU =========================
# Função: menu principal do sistema
def menu():
    while True:
        print("""
=================================================
               DEVBASE - SISTEMA
=================================================

- USUÁRIO -
1 - Criar usuário
2 - Login
3 - Listar usuários
4 - Buscar usuário
5 - Atualizar usuário
6 - Deletar usuário

- CONTEÚDO -
7 - Criar tópico
8 - Listar tópicos
9 - Criar comentário

- INTERAÇÕES -
10 - Curtir (tópico/comentário)

- PERFIL -
11 - Criar perfil

- SISTEMA -
12 - Enviar feedback
13 - Criar notificação
14 - Registrar acesso diário
15 - Gerar recuperação de senha

- OUTROS -
0 - Sair

=================================================
""")

        opcao = input("Escolha: ")

        # ================= USUÁRIO =================
        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            autenticar_usuario()
        elif opcao == "3":
            listar_usuarios()
        elif opcao == "4":
            buscar_usuario()
        elif opcao == "5":
            atualizar_usuario()
        elif opcao == "6":
            deletar_usuario()

        # ================= CONTEÚDO =================
        elif opcao == "7":
            criar_topico()
        elif opcao == "8":
            listar_topicos()
        elif opcao == "9":
            criar_comentario()

        # ================= INTERAÇÕES =================
        elif opcao == "10":
            curtir()

        # ================= PERFIL =================
        elif opcao == "11":
            criar_perfil()

        # ================= SISTEMA =================
        elif opcao == "12":
            enviar_feedback()
        elif opcao == "13":
            criar_notificacao()
        elif opcao == "14":
            registrar_acesso()
        elif opcao == "15":
            gerar_recuperacao_senha()

        # ================= SAIR =================
        elif opcao == "0":
            print("A DevBase agradece! Saindo do sistema... ")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()


