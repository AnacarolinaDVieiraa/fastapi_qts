from app.descontos.descontos import calcular_desconto

def test_valor_invalido_negativo():
    resultado = calcular_desconto(-50.0, cliente_vip=True)
    assert resultado == 0

def test_cliente_vip_com_valor_valido():
    resultado = calcular_desconto(100.0, cliente_vip=True)
    assert round(resultado, 3) == 20.0

def test_cliente_nao_vip_com_valor_valido():
    resultado = calcular_desconto(100.0, cliente_vip=False)
    assert round(resultado, 3) == 10.0

def test_valor_positivo_muito_pequeno():
    resultado_normal = calcular_desconto(0.01, cliente_vip=False)
    assert round(resultado_normal, 3) == 0.001
    
    resultado_vip = calcular_desconto(0.01, cliente_vip=True)
    assert round(resultado_vip, 3) == 0.002

def test_valor_maior():
    assert round(calcular_desconto(200.0, cliente_vip=True), 3) == 40.0
    assert round(calcular_desconto(200.0, cliente_vip=False), 3) == 20.0