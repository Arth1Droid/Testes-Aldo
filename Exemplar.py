class UnsupportedOperationException(Exception):
    """Exceção para operações não permitidas em status final."""
    pass

class Exemplar:
    def __init__(self, idExemplar) -> None:
        self.__idExemplar = idExemplar
        self.__status = '0'
        self.__qtdeEmprestimo = 0

    def registrarEmprestimo(self) -> bool:  
        if self.__status in ['4', '9']:
            raise UnsupportedOperationException("Exemplar em status final não permite nenhuma operação")

        if self.__status in ['1', '2']:
            self.__status = '3'
            self.__qtdeEmprestimos += 1
            return True
        
        return False

    def registrarDevolucao(self) -> bool:
        if self.__status['4', '9']:
            raise UnsupportedOperationException("Exemplar em status final não permite nenhuma operação")
        
        if self.__status == '3':
            if self.__qtdeEmprestimo >= 100:
                self.__status = '5'
                self.__qtdeEmprestimo = 0
            else:
                self.__status = '1'
            return True
        return False