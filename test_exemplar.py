import pytest
from Exemplar import Exemplar

def test_descartar_exemplar_disponivel():
    # Arrange
    exemplar = Exemplar(1)
    exemplar.setStatus('1')

    # Act
    novoStatus = exemplar.alterar_status('9')

    # Assert
    assert novoStatus is True
    assert exemplar.getStatus() == '9'

def test_disponibilizar_exemplar_emprestado():
    # Arrange
    exemplar = Exemplar(1)
    exemplar.setStatus('3') 

    # Act
    resultado = exemplar.alterar_status('1')  

    # Assert
    assert resultado is False
    assert exemplar.getStatus() == '3'  


def test_colocar_perdido_exemplar_emprestado():

    #Arrange 
    status_Esperado = '4' 
    exemplar = Exemplar(1) 
    exemplar._Exemplar__status = '3' 

    #Act 
    novo_Status = exemplar.alterar_status('4')
    status_Obtido = exemplar.getStatus() 

    #Assert 
    assert status_Obtido == status_Esperado
    assert novo_Status is True

def test_disponibilizar_exemplar_restauracao():

    """
    CT028 - Disponibilizar um exemplar que está em restauração
    """

    #Arrange 
    status_Esperado = '1' 
    exemplar = Exemplar(2) 
    exemplar._Exemplar__status = '5' 

    #Act 
    novo_Status = exemplar.alterar_status('1')
    status_Obtido = exemplar.getStatus() 

    #Assert 
    assert status_Obtido == status_Esperado
    assert novo_Status is True

def test_disponibilizar_exemplar_descartado():
    # Arrange
    esperado = "Exemplar em status final não permite nenhuma operação"
    exemplar = Exemplar(2) 
    exemplar.setStatus('9') 

    # Act
    with pytest.raises(Exception) as excinfo:
        exemplar.alterar_status('1')
    
    # Assert
    assert esperado in str(excinfo.value) 