from tabuleiro import Tabuleiro


tabuleiro = Tabuleiro()

tabuleiro.preencher_tabuleiro()

tabuleiro.print_tabuleiro()

print(len(tabuleiro.get_json_tabuleiro()['data']))

for number in tabuleiro.get_json_tabuleiro()['data']:
    print(number)
