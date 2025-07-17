def formata_preco(valor):
    if valor == 0:
        return ""
    return f"R$ {valor:.2f}".replace('.', ',')
