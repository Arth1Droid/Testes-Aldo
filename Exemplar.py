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
            self.__qtdeEmprestimo += 1
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
    
    def alterarStatus(self, novo_status: str) -> str:
        if self.__status in ['4', '9']:
            raise UnsupportedOperationException("Exemplar em status final não permite nenhuma operação")

        status_atual = self.__status

        if status_atual in ['0', '2']:
            self.__status = '1'

        elif status_atual == '1':
            if novo_status in ['2', '5', '9']:
                self.__status = novo_status
            else:
                raise ValueError("Novo status inválido para o status atual")

        elif status_atual == '3':
            if novo_status == '4':
                self.__status = '4'
            else:
                raise ValueError("Novo status inválido para o status atual")

        elif status_atual == '5':
            if novo_status in ['1', '2']:
                self.__status = novo_status
            else:
                raise ValueError("Novo status inválido para o status atual")

        else:
            return '0'

        return self.__status
    
    def getIdExemplar(self) -> int:
        return self.__idExemplar
    
    def getStatus(self) -> str:
        return self.__status
    
    def getQtdeEmpretimo(self) -> int:
        return self.__qtdeEmprestimo