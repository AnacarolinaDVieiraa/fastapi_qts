import pytest
import time
from app.faturamento.cobranca import processar_cobranca

@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, valor_esperado",
    [
        (0.0, "BASICO", 0, -1.0),      
        (100.0, "PREMIUM", -1, -1.0),
        (-50.0, "EMPRESARIAL", 10, -1.0), 
        (100.0, "INVALIDO", 0, -2.0),  
    ],
)
def test_entradas_invalidas_e_planos(valor_base, plano, dias_atraso, valor_esperado):
    resultado = processar_cobranca(valor_base, plano, dias_atraso)
    assert resultado == valor_esperado

def test_valores_de_cobranca_validos():
    assert processar_cobranca(100.0, "PREMIUM", 0) == 90.0
    assert processar_cobranca(100.0, "EMPRESARIAL", 0) == 80.0
    assert processar_cobranca(100.0, "PREMIUM", 1) == 95.45
    assert processar_cobranca(100.0, "BASICO", 31) == 156.00
