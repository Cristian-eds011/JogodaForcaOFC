from random import choice

def caracteres_nulos(palavra):
    total_nulos = 0
    for i in palavra:
        if i == '-' or i == ' ':
            total_nulos += 1
    return total_nulos

def define_jogador_desafiado_desafiador(jogador1, jogador2):
    if not jogador1.get('desafiado') and not jogador2.get('desafiado'):
        escolhido = choice([jogador1, jogador2])
        escolhido['desafiado'] = True
    else:
        if jogador1.get('desafiado'):
            jogador1['desafiado'] = False
            jogador2['desafiado'] = True
        elif jogador2.get('desafiado'):
            jogador2['desafiado'] = False
            jogador1['desafiado'] = True


def obtem_jogador_desafiado(jogador1, jogador2):
    return jogador1 if jogador1.get('desafiado') else jogador2


def obtem_jogador_desafiador(jogador1, jogador2):
    return jogador1 if not jogador1.get('desafiado') else jogador2
    

def erro_ou_acerto(letra, palavra):
    return 'Acertou' if letra in palavra else 'Errou'


def ganhador_jogo(jogador1, jogador2):
    if jogador1['pontos'] > jogador2['pontos']:
        print(f'\033[31mJOGADOR {jogador1["nome"]} VENCEU O JOGO!!\033[m')
    elif jogador1['pontos'] == jogador2['pontos']:
        print('\033[31mO JOGO ACABOU EMPATADO!\033[m')
    elif jogador1['pontos'] < jogador2['pontos']:
        print(f'\033[31mJOGADOR {jogador2["nome"]} VENCEU O JOGO!!\033[m')


