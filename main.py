from IPython.display import clear_output
import matplotlib.pyplot as plt
import numpy as np
import random

global posAPAx
global posAPAy


def exibir(matriz):
    clear_output(wait=True)
    plt.imshow(matriz, "gray")
    plt.nipy_spectral()
    plt.plot([posAPAy], [posAPAx], marker="o", color="r", ls="")
    # plt.show(block=False)
    plt.draw()
    plt.pause(0.5)
    plt.clf()


def criar_matriz(rows: int = 4, columns: int = 4) -> np.ndarray:
    if rows < 3 or columns < 3:
        raise ValueError("Matriz deve ter tamanho mínimo 3x3")
    matriz = np.ones((rows + 2, columns + 2), dtype=np.int64)
    matriz[1:-1, 1:-1] = 0
    return matriz


def espalhar_sujeira(matriz: np.ndarray, qtd_sujeira=None) -> np.ndarray:
    rows, columns = len(matriz) - 2, len(matriz[0]) - 2  # Ignora bordas

    if qtd_sujeira is None:  # No máximo metade da matriz
        qtd_sujeira = random.randint(1, (rows * columns) // 2)

    while qtd_sujeira > 0:
        x = random.randint(1, rows)
        y = random.randint(1, columns)
        if matriz[x, y] == 1 or matriz[x, y] == 2:
            continue
        matriz[x, y] = 2
        qtd_sujeira -= 1
    return matriz


def get_pos_distancia(
    ponto_inicial: tuple[int, int], distancia: int
) -> list[tuple[int, int]]:
    abs(distancia)
    if distancia == 0:
        return [ponto_inicial]
    x, y = ponto_inicial
    a, b = distancia, 0
    positions = [(x + a, y + b), (x - a, y - b), (x + b, y + a), (x - b, y - a)]
    a, b = a - 1, b + 1
    while a > 0:
        positions.extend(
            [(x + a, y + b), (x + a, y - b), (x - a, y - b), (x - a, y + b)]
        )
        a, b = a - 1, b + 1
    # Valores negativos filtrados
    positions = list(filter(lambda pos: not (pos[0] < 0 or pos[1] < 0), positions))
    positions.sort()
    return positions


def check_out_of_bounds(matriz: np.ndarray, pos: tuple[int, int]) -> bool:
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(matriz) or pos[1] >= len(matriz[0])


def verifica_sujeira(matriz: np.ndarray, posicoes: list[tuple[int, int]]):
    for pos in posicoes:
        try:
            if matriz[pos] == 2:
                return pos
        except IndexError:
            pass
    return


def radar(matriz: np.ndarray, ponto_inicial: tuple[int, int]) -> tuple[int, int]:
    """Retorna a posição da sujeira mais próxima do ponto inicial"""
    rows, columns = len(matriz) - 2, len(matriz[0]) - 2  # Ignora bordas
    max_distance = (rows - 1) + (columns - 1)
    for distancia in range(max_distance + 1):
        posicoes = get_pos_distancia(ponto_inicial, distancia)
        sujeiras = verifica_sujeira(matriz, posicoes)
        if sujeiras:
            return sujeiras
    return tuple()


def count(func):
    def wrapper(*args, **kwargs):
        global pontos
        func(*args, **kwargs)
        pontos += 1

    return wrapper


@count
def esquerda():
    global posAPAy
    posAPAy -= 1
    # print("Movendo esquerda")


@count
def direita():
    global posAPAy
    posAPAy += 1
    # print("Movendo direita")


@count
def acima():
    global posAPAx
    posAPAx -= 1
    # print("Movendo acima")


@count
def abaixo():
    global posAPAx
    posAPAx += 1
    # print("Movendo abaixo")


@count
def aspirar(matriz: np.ndarray, pos: tuple[int, int]) -> bool:
    """Retorna se a operação foi de fato realizada"""
    if matriz[pos[0], pos[1]] == 2:
        matriz[pos[0], pos[1]] = 0
        # print("Aspirando")
        return True
    return False


def checkObj(sala: np.ndarray) -> bool:
    return bool(np.any(sala == 2))


def agenteObjetivo(
    percepcao: tuple, objObtido: bool, posObjetivo: tuple[int, int]
) -> str:
    # percepcao = ((posAPAx, posAPAy), status)
    status = percepcao[1]
    if status == "sujo":
        return "aspirar"

    x, y = percepcao[0]

    if objObtido:
        if y > posObjetivo[1]:
            return "esquerda"
        if y < posObjetivo[1]:
            return "direita"
        if x > posObjetivo[0]:
            return "acima"
        if x < posObjetivo[0]:
            return "abaixo"

    return "NoOp"


if __name__ == "__main__":
    # Criar matriz
    matriz = espalhar_sujeira(criar_matriz())
    rows, columns = len(matriz) - 2, len(matriz[0]) - 2

    # Posição inicial
    posAPAx = 1  # random.randint(1, rows)
    posAPAy = 1  # random.randint(1, columns)
    pontos = 0
    exibir(matriz)

    mover = {
        "esquerda": esquerda,
        "direita": direita,
        "acima": acima,
        "abaixo": abaixo,
    }

    while checkObj(matriz):
        status = "sujo" if matriz[posAPAx, posAPAy] == 2 else "limpo"
        acao = agenteObjetivo(
            ((posAPAx, posAPAy), status),
            checkObj(matriz),
            radar(matriz, (posAPAx, posAPAy)),
        )

        if acao == "aspirar":
            aspirar(matriz, (posAPAx, posAPAy))
            exibir(matriz)
        elif acao == "NoOp":
            print("Sem operação")
        else:
            mover[acao]()
            exibir(matriz)

    print("Pontos ->", pontos)
