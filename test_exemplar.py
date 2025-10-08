import pytest
from Exemplar import Exemplar


def test_disponibilizar_exemplar_emprestado():
    # Arrange
    exemplar = Exemplar(1)
    exemplar.setStatus('3') 

    # Act
    resultado = exemplar.alterar_status('1')  

    # Assert
    assert resultado is False
    assert exemplar.getStatus() == '3'  