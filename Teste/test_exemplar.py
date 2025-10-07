from Exemplar import Exemplar

def test_CT027():

    """
    CT027 - Colocar como perdido um exemplar que está emprestado
    """

    #Arrange 
    status_Esperado = '4' 
    exemplar = Exemplar(1) 
    exemplar._Exemplar__status = '3' 

    #Act 
    novo_Status = exemplar.alterarStatus('4')
    status_Obtido = exemplar.getStatus() 

    #Assert 
    assert status_Obtido == status_Esperado
    assert novo_Status is True

def test_CT028():

    """
    CT028 - Disponibilizar um exemplar que está em restauração
    """

    #Arrange 
    status_Esperado = '1' 
    exemplar = Exemplar(2) 
    exemplar._Exemplar__status = '5' 

    #Act 
    novo_Status = exemplar.alterarStatus('1')
    status_Obtido = exemplar.getStatus() 

    #Assert 
    assert status_Obtido == status_Esperado
    assert novo_Status is True