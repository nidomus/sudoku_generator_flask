from random import shuffle
import copy


class BlockedException(Exception):
    pass


class Quadrante():

    def __init__(self, numero) -> None:

        self.numero = numero
        self.matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.vizinhos_v: list[Quadrante] = []
        self.vizinhos_h: list[Quadrante] = []

    # PREENCHE A MATRIZ DO QUADRANTE SEGUINDO AS REGRAS DO SUDOKU
    def preencher_matriz(self):
        cont = 0
        while self.verificar_quadrante(0):

            self.matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            shuffle(numeros)

            for linha in range(3):

                for coluna in range(3):
                    for num in numeros:
                        if not self.verificar_vizinhos(num, linha, coluna):
                            self.matriz[linha][coluna] = num
                            numeros.remove(num)
                            break

            if len(numeros) > 0:
                raise BlockedException

    def get_restantes(self,):

        valores = []
        for i in self.matriz:
            for j in i:
                valores.append(j)

        completa = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        resta = []
        for x in completa:
            if x not in valores:
                resta.append(x)

        return resta

    # VERIFICA SE O VALOR SORTEADO JÁ ESTÁ PRESENTE NA MATRIZ

    def verificar_quadrante(self, valor):

        for linha in self.matriz:
            if valor in linha:
                return True

        return False

    def encontrar_valores_invalidos(self, valor, linha, coluna):
        coordenadas = []

        for vizinho in self.vizinhos_h:
            aux = vizinho.verificar_linha(valor, linha)
            if aux is not None:
                coordenadas.append(aux)

        for vizinho in self.vizinhos_v:
            aux = vizinho.verificar_coluna(valor, coluna)
            if aux is not None:
                coordenadas.append(aux)
        return coordenadas

    # VERIFICA SE O VALOR SORTEADO OBEDECE A REGRA DOS VIZINHOS NO SUDOKU
    def verificar_vizinhos(self, valor, linha, coluna):

        for vizinho in self.vizinhos_h:
            if vizinho.verificar_linha(valor, linha) is not None:
                return True

        for vizinho in self.vizinhos_v:
            if vizinho.verificar_coluna(valor, coluna) is not None:
                return True

        return False

    def quantidade_valor(self, valor):
        qtd = 0
        for linha in range(3):
            for coluna in range(3):
                if self.matriz[linha][coluna] == valor:
                    qtd += 1
        return qtd

    def verificar_linha(self, valor, linha):
        if valor in self.matriz[linha]:
            i = linha
            j = self.matriz[linha].index(valor)
            return (self.numero, i, j)
        return None

    def verificar_coluna(self, valor, coluna):
        for linha in self.matriz:
            if valor == linha[coluna]:
                i = self.matriz.index(linha)
                j = coluna
                return (self.numero, i, j)
        return None

    def coordenada_absoluta(self, i, j):
        if self.numero < 3:
            a = 0
        elif self.numero < 6:
            a = 3
        else:
            a = 6

        abs_i = i + a
        abs_j = j + 3 * (self.numero - a)

        return (abs_i, abs_j)

    def set_vizinhos_h(self, vizinhos):

        self.vizinhos_h = vizinhos

    def set_vizinhos_v(self, vizinhos):

        self.vizinhos_v = vizinhos

    def __str__(self) -> str:

        string = ''

        for list in self.matriz:

            for number in list:

                string += str(number) + ' '
            string += '\n'

        return string
