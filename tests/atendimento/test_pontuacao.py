from app.atendimento.pontuacao import calcular_pontuacao_atendimento,classificar_atendimento

def test_tempo_minutos_igual_a_zero():
    assert calcular_pontuacao_atendimento (0,True,True)==0

def test_tempo_minutos_negativo():
    assert calcular_pontuacao_atendimento (-3, False,True)==0

def test_tempo_minutos_igual_a_dez():
    assert calcular_pontuacao_atendimento (10,True,False)==10

    
