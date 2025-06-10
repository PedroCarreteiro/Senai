class ItemBiblioteca:
    def __init__(self, titulo: str, ano_publicacao: int, disponivel: bool = True):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel
        if (ano_publicacao is not int) and (ano_publicacao <= 0):
            print("Ano de publicação inválido!")
        else:
            self.ano_publicacao = ano_publicacao

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print("Livro emprestado")
        else:
            print("Este livro já foi emprestado!")

    def devolver(self):
        if self.disponivel:
            print("Este livro já está disponível!")
        else:
            self.disponivel = True
            print("Livro devolvido!")
            
    def obter_info(self):
        # return {
        #     "titulo": self.titulo,
        #     "ano_publicacao": self.ano_publicacao,
        #     "disponivel": self.disponivel
        # }
        print(f"\nNome da coleção: {self.titulo}")
        print(f"Ano: {self.ano_publicacao}")
        if self.disponivel:
            print("Disponível: Sim")
        else:
            print("Disponível: Não")

class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int, disponivel: bool = True):
        super(). __init__(titulo, ano_publicacao, disponivel) 
        self.lista_livros = []

    def adicionar_livro(self, livro: ItemBiblioteca):
        self.lista_livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        #verifcar se há algum item indisponível
        for livro in self.lista_livros:
            if not livro.disponivel:
                return False 
        return True

    def obter_info(self):
        super().obter_info()        
        print(f"\nNome da coleção: {self.titulo}"
              f"\nAno: {self.ano_publicacao}")
        
        if self.disponivel:
            print("Disponível: Sim")
        else:
            print("Disponível: Não")

        print("Livros da coleção: ")
        
        for i in range(len(self.lista_livros)):
            print(self.lista_livros[i].titulo)


class Revista(ItemBiblioteca):
    def __init__(self, edicao: int, titulo: str, ano_publicacao: int, disponivel: bool = True):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.edicao = edicao

    def atualizar_edicao(self, nova_edicao):
        nova_edicao = int(input("Digite o número da nova edição: "))
        if nova_edicao > 0:
            self.edicao = nova_edicao
        else:
            print("Número de edição inválido!")




livro1 = ItemBiblioteca("livro1", 2004, True)
livro2 = ItemBiblioteca("livro2", 2005, True)
livro3 = ItemBiblioteca("livro3", 2043, False)

livro1.emprestar()
livro1.devolver()
livro1.obter_info()


colecao = ColecaoLivros("Colecao1", 2010, True)
colecao.adicionar_livro(livro1)
colecao.adicionar_livro(livro2)
colecao.adicionar_livro(livro3)

colecao.obter_info()

