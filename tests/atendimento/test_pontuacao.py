from app.atendimento.pontuacao import calcular_pontuacao_atendimento,classificar_atendimento

def test_tempo_minutos_igual_a_zero():
    assert calcular_pontuacao_atendimento (0,True,False)==0

def test_tempo_minutos_negativo():
    assert calcular_pontuacao_atendimento (-3, False,True)==0

def test_tempo_minutos_igual_a_dez():
    assert calcular_pontuacao_atendimento (10,True,False)==10

def test_tempo_minutos_igual_a_onze():
    assert calcular_pontuacao_atendimento (11, True,False)==8

def test_tempo_minutos_igual_a_vinte_e_um():
    assert calcular_pontuacao_atendimento (21,True,True)==4

def test_tempo_minutos_igual_menor_que_10():
    assert calcular_pontuacao_atendimento (10,False,False)==5

def test_tempo_minutos_igual_a_quinze():
    assert calcular_pontuacao_atendimento(15,False,True)==1

def test_tempo_minutos_igual_a_vinte_e_cinco():
    assert calcular_pontuacao_atendimento(25,False,True)==0

def test_fluxo_completo_classificacao_excelente():
    assert classificar_atendimento(calcular_pontuacao_atendimento(20, True, False)) == "Excelente"

def test_fluxo_completo_classificacao_bom():
    assert classificar_atendimento(calcular_pontuacao_atendimento(11, True, False)) == "Bom"

def test_fluxo_completo_classificacao_regular():
    assert classificar_atendimento(calcular_pontuacao_atendimento(10, False, False)) == "Regular"

def test_fluxo_completo_classificacao_critico():
    assert classificar_atendimento(calcular_pontuacao_atendimento(15, False, True)) == "Crítico"