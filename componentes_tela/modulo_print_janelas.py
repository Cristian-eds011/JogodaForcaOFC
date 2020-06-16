from time import sleep
from componentes_tela.modulo_inputs import escolha_menu
import os

def print_linha(num):
    print('-' * num)


def print_palavra_forca(mostrar_palavra, letras_certas):
    for c in mostrar_palavra:
        if c == '-':
            print(f' {"-"}', end=' ')
        elif c == ' ':
            print('  ', end=' ')
        elif c in letras_certas:
            print(f' {c}',end=' ')
        else:
            print(f' {"_"}', end=' ')
    print()


def menu():
    print('=' *30)
    print('| BEM VINDO AO JOGO DA FORCA |')
    print('='*30)
    print('\033[31m[I] Iniciar\033[m')
    print('\033[32m[R] Regras\033[m')
    print('\033[33m[S] Sair\033[m')
    escolha = escolha_menu()
    if escolha == 'I':
        print('Iniciando...')
        sleep(3)
    elif escolha == 'R':
        print_linha(30)
        print('Jogo da forca consiste em 2 jogadores.')
        print('Ao informar o nome dos dois jogadores, será sorteado qual virará o DESAFIADO e o DESAFIADOR')
        print('O jogador DESAFIADOR escolherá uma palavra, seguinte de uma dica para o jogador DESAFIADO')
        print('O qual tentará adivinhar a palavra, antes dos 6 erros.')
        print('O jogo é composto por turnos, ganha quem terminar com mais pontos.')
        print_linha(30)
        retornar = 'n'
        while retornar != 'S':
            retornar = input('(S) para voltar ao menu: ').upper()
        print('Voltando...')
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        return menu()
    elif escolha == 'S':
        print('Saindo...')
        exit()


def desenha_jogo(erros):
    if erros == 0:
        print()
        print("|_____ ")
        print("|/   | ")
        print("|     ")
        print("|   ")
        print("|   ")
        print("|   ")
    elif erros == 1:
        print()
        print("|_____ ")
        print("|/   | ")
        print("|    \033[31mO\033[m ")
        print("|   ")
        print("|   ")
        print("|   ")
    elif erros == 2:
        print()
        print("|_____ ")
        print("|/   | ")
        print("|    \033[31mO\033[m ")
        print("|    \033[31m|\033[m")
        print("|   ")
        print("|   ")
    elif erros == 3:
        print()
        print("|_____ ")
        print("|/   | ")
        print("|    \033[31mO\033[m ")
        print("|   \033[31m/|\033[m")
        print("|   ")
        print("|   ")
    elif erros == 4:
        print()
        print("|_____ ")
        print("|/   | ")
        print("|    \033[31mO\033[m ")
        print("|   \033[31m/|\\\033[m")
        print("|   ")
        print("|   ")
    elif erros == 5:
        print()
        print("|_____ ")
        print("|/   | ")
        print("|    \033[31mO\033[m ")
        print("|   \033[31m/|\\\033[m")
        print("|   \033[31m/\033[m")
        print("|   ")
    elif erros == 6:
        print()
        print("|_____ ")
        print("|/   | ")
        print("|    \033[31mO\033[m ")
        print("|   \033[31m/|\\\033[m ")
        print("|    \033[31m|\033[m ")
        print("|   \033[31m/ \\\033[m ")


def ganhador_rodada(jogador):
    print(f'\033[32mO jogador {jogador} ganhou a Rodada!!\033[m')


def mostrar_pontos(jogador1, jogador2):
    print_linha(30)
    print(f'\033[36mPONTOS {jogador1["nome"]}: {jogador1["pontos"]}\033[m')
    print(f'\033[35mPONTOS {jogador2["nome"]}: {jogador2["pontos"]}\033[m')
    print_linha(30)


def dica_tamanho_palavra(dica, tamanho):
    print(f'\033[34mDICA: {dica}')
    print(f'A palavra tem {len(tamanho)} letras\033[m')