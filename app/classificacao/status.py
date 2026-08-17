def calcular_status_pedido(valor_total: float, pago: bool) ->str:
    if valor_total <= 0:
        return "INVALIDO"
    if not pago:
        return "PENDENTE"
    return "CONFIRMADO"

#invalido
#pendente
#confirmado

