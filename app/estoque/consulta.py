import time


def consultar_estoque(codigo_produto: str) -> int:
    """Consulta a quantidade de itens no estoque a partir de um código."""
    if not codigo_produto or len(codigo_produto) != 5:
        return -1

    if not codigo_produto.startswith("P"):
        return -1

    # Simula o tempo de consulta em um banco de dados legado
    time.sleep(0.06)

    if codigo_produto == "P0001":
        return 15
    if codigo_produto == "P0002":
        return 0

    return 5