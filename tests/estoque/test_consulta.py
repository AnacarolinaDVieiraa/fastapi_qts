import time 
import pytest 

from app.estoque.consulta import consultar_estoque

@pytest.mark.parametrize(

"codigo_produto,esperado",
[
    ("0123",-1),
    ("P00001",-1),
    ("", -1),
    ("00234", -1),
    ("P0001", 15),
    ("P0002", 0),
    ("P87A6", 5),

],

)

def test_consultar_estoque_funcional(codigo_produto,esperado):
    resultado = consultar_estoque(codigo_produto)
    assert resultado == esperado

def test_tempo_esperado():
    inicio = time.perf_counter()
    consultar_estoque ("P0001")
    fim = time.perf_counter()
    tempo_total = fim - inicio
    assert tempo_total < 0.1
    

