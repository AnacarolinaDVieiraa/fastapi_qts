def calcular_pontuacao_atendimento(tempo_minutos: int, resolvido_primeiro_contato: bool, reincidencia: bool) -> int:
            ##menor ou igual a 0 
    if tempo_minutos <= 0:
        return 0
    base = 0
            ##menor ou igual a 10
    if resolvido_primeiro_contato:
        if tempo_minutos <= 10:
            base = 10
            #entre dois valores
        if 11 <= tempo_minutos <= 20:
            base = 8
            #maior que 20 
        if tempo_minutos > 20:
            base = 6
            
    if not resolvido_primeiro_contato:
            ##menor ou igual a 10
        if tempo_minutos <= 10:
            base = 5
            ##entre dois valores 
        if 11 <= tempo_minutos <= 20:
            base = 3
            ##maior que 20
        if tempo_minutos > 20:
            base = 1

    if reincidencia:
        base -= 2

    if base < 0:
        return 0
        
    return base


def classificar_atendimento(pontuacao: int) -> str:
    if pontuacao >= 9:
        return "Excelente"
        
    if pontuacao >= 7:
        return "Bom"
        
    if pontuacao >= 4:
        return "Regular"
        
    return "Crítico"