class Exemplar:
    def __init__(self, idExemplar):
        self.__idExemplar = idExemplar
        self.__status = '0'
        self.__qtdeEmprestimo = 0

    def setStatus(self, status):
        self.__status = status

    def setQtdeEmprestimos(self, qtde):
        self.__qtdeEmprestimo = qtde

    def getStatus(self):
        return self.__status

    def getQtdeEmprestimo(self):
        return self.__qtdeEmprestimo
