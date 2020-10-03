class Cliente:
    def __init__(self, nome):
        self.__nome = nome;

    @property  # a @property nos permite utilizar a função nome sem parenteses
    def nome(self):  # o nome do método deve ser o mesmo que o do atributo
        return self.__nome.title()  # a função title() retorna a string com a primeira letra maiúscula

    @nome.setter
    def nome(self, nome):
        self.__nome = nome