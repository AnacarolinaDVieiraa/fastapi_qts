def classificador_nota(nota: float) -> str:
    if nota < 0 or  nota > 10:
        return "NOTA INVALIDA"
    if nota >= 7:
        return "APROVADO"
    if nota >= 5:
        return "RECUPERACAO"
    return "REPROVADO"