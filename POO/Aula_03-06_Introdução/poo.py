class Pessoa:
    def __init__(self, nome, idade): #self é uma referência à instâcia atual, usada para acessar variáveis quue pertencem a classe
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá \nMeu nome é {self.nome} e teho {self.idade} anos")

    def __str__(self): #transformar a classe pessoa em string sempre que eu for utilizar a classe como string
        return f"Pessoa com o nome de {self.nome}"

    def __eq__(self,other): #comparar se classe é igual. o other é com quem eu estou comparando
        if isinstance(other,Pessoa):#ver se é uma classe pessoa mesmo que eu estou comparando
            if self.nome == other.nome and self.idade == other.idade:
                return True
        return False

    """
    __str__ -> transformar a classe em string
    __ge__ -> >=
    __gt__ -> >
    __le__ -> <=
    __lt__ -> <
    __eq__ -> ==
    __len__ -> falar o tamanho do dado em caractere
    to_dict -> transformar dados da classe em dicionário
    """


    def __len__(self): #verificar tamanho
        return self.idade

    def to_dict(self): #transformar em dicionario
        return {
            "nome": self.nome,
            "idade": self.idade
        }

pessoa1 = Pessoa("Pedo",11)
# pessoa1.apresentar()
# print(pessoa1)
#
pessoa2 = Pessoa("João",55)
#
# if pessoa1 == pessoa2:
#     print("São iguais")
# else:
#     print("São diferentes")
#
# dicionario = pessoa1.to_dict()
# print(dicionario)


# ==== Herança e Polimorfismo ==== #

class Funcionario(Pessoa):
    #se não tiver nada de diferente, esvreve só "pass"
    def __init__(self,nome,idade,cargo):
        super().__init__(nome,idade) #herdar de outra classe
        self.cargo = cargo #novo dessa classe
    def apresentar(self):
        #super().apresentar()  # apresentar do jeito da outra classe
        print(f"Olá, eu sou {self.nome}, tenho {self.idade} anos e sou {self.cargo}")


funcionario = Funcionario("Kauan",19, "Aprendiz")
lista_pessoas = [pessoa1,pessoa2,funcionario]

# for pessoa in lista_pessoas:
#     pessoa.apresentar()

#print(funcionario.nome)

# funcionario.nome = "Luis"
# print(funcionario.nome)

# ==== Encapsulamento === #

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular #atriuto público
        self.__saldo = saldo #atributo encapsulado
    # def get_saldo(self):
    #     return self.__saldo
    #
    # def set_saldo(self,valor):
    #     if valor < 0:
    #         raise ValueError("Saldo não pode ser negativo") #tratando erro
    #     self.__saldo = valor

    @property #decorator que vai pegar as informações desse atributo
    def saldo(self):
        return self.__saldo

    @saldo.setter #setter para setar algo
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo") #tratando erro
        self.__saldo = valor

minha_conta = ContaBancaria("Dorival", 1000)
# minha_conta.__saldo = 4000
#print(minha_conta.__saldo) #ele imprime o novo valor (4000), mas se for tentar o original (1000) da erro
#minha_conta.set_saldo(5000)
#print(minha_conta.get_saldo()) #vai pegar o valor original pelo get_saldo se não tiver sido alterado no meio
minha_conta.saldo = 5000
print(minha_conta.saldo)

# ==== Abstração ==== #

from abc import ABC, abstractmethod #import biblioteca de abstração

class Pagamento(ABC):

    @abstractmethod
    def autorizar(self, valor): #toda classe que herdar pagamento, vai ter que herdar autorizar
        pass

    @abstractmethod
    def estornar(self, valor): #toda classe que herdar pagamento, vai ter que herdar estornar
        pass

class Pix(Pagamento):
    def autorizar(self, valor):
        print(f"Transferindo valor R${valor} via PIX...")

    def estornar(self, valor):
        print(f"Devolvendo R${valor} via PIX...")

Pix().autorizar(100)