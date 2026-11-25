"""A01: complete somente a função. Dados fictícios."""


def itens_disponiveis(equipamentos, limite):
    veqp = equipamentos
    neqp = []
    lmt = limite
    for e in veqp:
        if e["quantidade"] >= lmt:
            neqp.append(e["nome"])
    # TODO: devolver, na ordem original, os nomes com quantidade maior ou igual ao limite.
    # Lacuna intencional: None faz o programa mostrar PENDENTE.
    return neqp


equipamentos = [
    {"nome": "Notebook", "quantidade": 3},
    {"nome": "Projetor", "quantidade": 0},
    {"nome": "Cabo", "quantidade": 5},
]

if __name__ == "__main__":
    for registros, limite in [(equipamentos, 1), (equipamentos, 4), ([], 1)]:
        resultado = itens_disponiveis(registros, limite)
        print("Limite", limite, "=>", "PENDENTE" if resultado is None else resultado)
