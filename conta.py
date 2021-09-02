#Em Orientação a Objetos, as variáveis são denominadas: referências.Teremos uma referência, uma classe, uma construção de objeto
#__init__ funcao construtora em outras linguagem funcao construtor
#"vai para esse objeto e acessa aquele atributo". O pedido de "vai" nas linguagens Orientadas a Objeto é indicado com . exemplo: conta.titular
#encapsulamento =   A ação de tornar privado o acesso aos atributos, no mundo Orientado a Objetos, chamamos de encapsulamento:underscore (__)

class Conta:
    def __init__(self, numero, titular, saldo, limite): #para criar objeto na memoria, referencia usamos a variavel self = referencia.Os atributos são as características que especificam uma classe(numero, titular,saldo,limite).
        print("Construindo objeto...{}".format(self)) #self é a referência que sabe encontrar o objeto construído em memória.
        self.__numero = numero #o caractere "ponto" (.) é um comando de ida ao objeto self.
        self.__titular = titular
        self.__saldo = saldo # para tornar a informacao privado, adicionando dois caracteres underscore (__).
        self.__limite = limite #o limite do objeto (self.limite) será o limite recebido do parâmetro da função __init__().


    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

#escapsulamento
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

#propriedades (property)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
#Esse métodos que conseguimos chamar sem uma referência (self)recebem o nome de estáticos,
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    

# outro exemplo da funcao GET(Getters) para devolver retornar
#    def get_saldo(self): #funcao devolve e retorna saldo
 #       return self.__saldo

#    def get_titular(self): #retorna titular
#        return self.__titular

        #    def get_limite(self): #retorna limite
        #return self.__limite

# funcao SET(setters) nunca retorna, so recebe

        #  def set_limite(self, limite):
# self.__limite = limite

#exemplo:
#    >> > from conta import Conta
    #   >> > conta = Conta(123, "Nico", 55.5, 1000.0)
    #Construindo
    #objeto... < conta.Conta
    #object at 0x10d92c160 >
    #>> > conta.get_limite()
    #1000.0
    #>> > conta.get_saldo()
    #55.5
    #>> > conta.get_titular()
    #'Nico'
    #>> > conta.set_limite(1000.0)
