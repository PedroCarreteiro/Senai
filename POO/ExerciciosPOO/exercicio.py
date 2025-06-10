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
            return {
                "nome": self.nome,
                "ano_publicacao": self.ano_publicacao,
                "disponivel": self.disponivel
            }
            print(f"Título: {self.nome}\n")
            print(f"Ano: {self.ano_publicacao}\n")
            if disponivel:
                print("Disponível: Sim\n")
            else:
                print("Disponível: Não")

class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int, disponivel: bool = True):
        super(). __init__(titulo, ano_publicacao, disponivel) 
        self.lista_livros = []

    def adicionar_livro(self, livro: ItemBiblioteca):
        self.lista_livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        #verifcar se há algum itemm indisponível
        for livro in self.lista_livros:
            if not livro.disponivel:
                return False 
        return True

    def obter_info(lista_livro):
        super().obter_info()
        for i in range (len(self.lista_livros)):
            print(self.lista_livros[i].titulo)


lista = [
            ItemBiblioteca("livro1", 2004, True),
            ItemBiblioteca("livro2", 2005, True),
            ItemBiblioteca("livro3", 2043, False)
        ]


lista.obter_info()

# for i in range (len(lista)):
#     print(lista[i].titulo)

# colecao = ColecaoLivros("Colecao", 7777, True)
# colecao.adicionar_livro("livro1", 2004, True)