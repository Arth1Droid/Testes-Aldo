class Exemplar:
    def __init__(self, idExemplar):
        self.__idExemplar = idExemplar
        self.__status = '0'
        self.__qtdeEmprestimo = 0

    def alterarStatus(self, novo_status):
        if self.__status == '3'and novo_status == '4':
            self.__status = novo_status
            return True
        
        if self.__status == '5'and novo_status == '1':
            self.__status = novo_status
            return True

        return False
        

    def setStatus(self, status):
        self.__status = status

    def setQtdeEmprestimos(self, qtde):
        self.__qtdeEmprestimo = qtde

    def getStatus(self):
        return self.__status

    def getQtdeEmprestimo(self):
        return self.__qtdeEmprestimo