import pytest
from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
"renda_mensal, score_credito,restrito,retorno_esperado",
[
   (0, 500, False, "renda invalida"),
   (-100, 500, False, "renda invalida"),
   (-1,-10,True,"renda invalida"),
   (1000, -1, False, "score invalido"),
   (2000, 3000, False, "score invalido"),
   (1000, 400, True, "reprovado"),
   (1000, 300,False,"reprovado"),
   (1000,500,False,"aprovado padrao"),
   (1000, 900,False,"aprovado premium"),
],


)
def test_classificador_fret_caixa_preta(
    renda_mensal, score_credito, restrito, retorno_esperado

    #PASSO 2
):
    assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado

    @pytest.mark.parametrize(
"renda_mensal, score_credito,restrito,retorno_esperado",
[
    # Renda no limite
        (0, 500, False, "renda invalida"),
        (0.01, 500, False, "aprovado padrao"),

        # Score no limite inferior
        (1000, -1, False, "score invalido"),
        (1000, 0, False, "reprovado"),

        # Transição entre reprovado e aprovado padrão
        (1000, 399, False, "reprovado"),
        (1000, 400, False, "aprovado padrao"),

        # Transição entre aprovado padrão e aprovado premium
        (1000, 699, False, "aprovado padrao"),
        (1000, 700, False, "aprovado premium"),

        # Score no limite superior
        (1000, 1000, False, "aprovado premium"),
        (1000, 1001, False, "score invalido"),
],


)
    
    
    def test_classificador_credito(
    renda_mensal, score_credito, restrito, retorno_esperado
):
      assert classificar_credito(renda_mensal, score_credito, restrito) == retorno_esperado