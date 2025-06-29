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
        print(f"\nNome do livro: {self.titulo}")
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
                self.disponivel = False
                return False 
        return True

    def obter_info(self):
        print(f"\nNome da coleção: {self.titulo}")
        print(f"Ano: {self.ano_publicacao}")
        if self.disponivel:
            print("Disponível: Sim")
        else:
            print("Disponível: Não")    

        print("Livros da coleção: ")
        
        for i in range(len(self.lista_livros)):
            print(self.lista_livros[i].titulo)


class Revista(ItemBiblioteca):
    def __init__(self, titulo: str, ano_publicacao: int, edicao: int, disponivel: bool = True):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.edicao = edicao

    def atualizar_edicao(self):
        nova_edicao = int(input("\nDigite o número da nova edição: "))
        if nova_edicao > 0:
            print("\nEdição atualizada!")
            self.edicao = nova_edicao
        else:
            print("\nNúmero de edição inválido!")

    def restringir_emprestimo(self):
        if self.disponivel == True:
            dias = int(input("\nDigite a quantidade de dias que você deseja emprestar a revista: "))
            if self.ano_publicacao >= 2000 and dias <= 10:
                print("\nVocê emprestou a revista!")
                self.disponivel = False
            elif self.ano_publicacao < 2000 and dias <= 7:
                print("\nVocê emprestou a revista!")
                self.disponivel = False
            else:
                print(f"\nVocê não pode emprestar a revista {self.titulo} pois esse número de dias ultrapassa o limite máximo de empréstimo determinado para esta revista.")
        else:
            print("\nA revista já está em empréstimo!")

    def obter_info(self):
        print(f"\nNome da revista: {self.titulo}")
        print(f"Ano: {self.ano_publicacao}")
        if self.disponivel:
            print("Disponível: Sim")
        else:
            print("Disponível: Não")
        print(f"A edição da revista é {self.edicao}")


class Biblioteca:
    def __init__(self):
        self.itens_dicionario = {}

    def adicionar_item(self, item: ItemBiblioteca):
        if item.titulo in self.itens_dicionario:
            print("\nItem já cadastrado na biblioteca!")
        else:
            self.itens_dicionario[item.titulo] = item
            print("\nItem adicionado a biblioteca!") 

    def remover_titulo(self, titulo):
        if titulo in self.itens_dicionario:
            del self.itens_dicionario[titulo]
            print("\nItem removido da biblioteca!")
        else:
            print("\nEste item não está contido na biblioteca!")

    def listar_itens_disponiveis(self):
        titulos_disponiveis = []
        for titulo, item in self.itens_dicionario.items():
            if item.disponivel:
                titulos_disponiveis.append(titulo)
        # print(f"\nTotal de itens disponíveis: {len(titulos_disponiveis)}")
        return titulos_disponiveis

    
    def contar_itens_emprestados(self):
        i = 0
        for item in self.itens_dicionario.values():
            if not item.disponivel:
                i += 1
        # print(f"\nTotal de itens emprestados: {i}")
        return i

class RelatorioBiblioteca:
    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def gerar_relatorio_completo(self):
        print("\nRelatório completo: ")
        for item in self.biblioteca.itens_dicionario.values():
            item.obter_info()

    def gerar_relatorio_disponibilidade(self):
        titulos_disponiveis = []
        for titulo, item in self.biblioteca.itens_dicionario.items():
            if item.disponivel:
                titulos_disponiveis.append(titulo)

        total_disponiveis = len(titulos_disponiveis)
        relatorio = "\nItens disponíveis:\n"
        for titulo in titulos_disponiveis:
            relatorio += f"- {titulo}\n"
        relatorio += f"\nTotal de itens disponíveis: {total_disponiveis}"
        print(relatorio)
    
    def gerar_relatorio_emprestimos(self):
        titulos_emprestados = []
        for titulo, item in self.biblioteca.itens_dicionario.items(): #items retorna chave e valor do dict
            if item.disponivel == False:
                titulos_emprestados.append(titulo)

        total_emprestados = len(titulos_emprestados)
        relatorio = "\nItens emprestados:\n"
        for titulo in titulos_emprestados:
            relatorio += f"- {titulo}\n"
        print(relatorio)

        emprestados = self.biblioteca.contar_itens_emprestados()
        total = 0
        for _ in self.biblioteca.itens_dicionario:
            total += 1

        if total > 0:
            proporcao = emprestados / total
        else:
            proporcao = 0

        print(f"Total de itens emprestados: {emprestados}"
              f"\nProporção de itens emprestados: {proporcao:.2f}"
              f"\nPorcentagem de itens emprestados: {proporcao*100}%")
        
        
# ==== Testes ====

#Item

livro1 = ItemBiblioteca("livro1", 2004, True)
livro2 = ItemBiblioteca("livro2", 2005, True)
livro3 = ItemBiblioteca("livro3", 2043, True)

livro1.emprestar()
livro1.devolver()
livro1.obter_info()

#Coleção
colecao = ColecaoLivros("Colecao1", 2010)
colecao.adicionar_livro(livro1)
colecao.adicionar_livro(livro2)
colecao.adicionar_livro(livro3)

colecao.verificar_disponibilidade_colecao()

colecao.obter_info()


#Revista
revista = Revista("Revista1",2031, 1)

revista.atualizar_edicao()
revista.restringir_emprestimo()
revista.obter_info()

#Biblioteca
biblioteca = Biblioteca()
biblioteca.adicionar_item(livro1)
biblioteca.adicionar_item(livro2)
biblioteca.adicionar_item(livro3)
biblioteca.remover_titulo("livro3")
biblioteca.adicionar_item(livro3)
biblioteca.adicionar_item(colecao)
biblioteca.adicionar_item(revista)

# biblioteca.listar_itens_disponiveis()
# biblioteca.contar_itens_emprestados()

#Relatório
relatorio = RelatorioBiblioteca(biblioteca)
relatorio.gerar_relatorio_completo()
relatorio.gerar_relatorio_disponibilidade()
relatorio.gerar_relatorio_emprestimos()
