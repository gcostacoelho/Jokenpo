import random as r
import os
import time
import colorama
from colorama import Fore

colorama.init(autoreset='True')

jogadas = ['Pedra', 'Papel', 'Tesoura']

def iniciaJogo():
    os.system('clear')
    print(Fore.GREEN + '#' * 20)
    print(Fore.GREEN + ' Bem vindo ao jogo')
    print(Fore.GREEN + '#' * 20)
    print('\n')

def comecaJogo():
    iniciaJogo()
    play = input("Deseja começar o jogo? (Sim/Não): ").lower()
    while True:
        if play == 'sim':
            print(Fore.CYAN + 'Iniciando...')
            time.sleep(1)
        
            jogadaBot = r.choice(jogadas)
            jogadaPlayer = verificaPlayer()
            
            time.sleep(1)
            botWin = bot(jogadaBot, jogadaPlayer)
            playerWin = player(jogadaBot, jogadaPlayer)
            defineGanhador(botWin, playerWin)

            playAgain = input('Deseja jogar novamente (Sim/Não)?R: ').lower()
            
            if playAgain == 'sim':
                os.system('clear')
                time.sleep(1)
            else:
                print(Fore.CYAN + '\nSaindo do jogo, obrigado por jogar :)')
                break
        else: 
            print(Fore.CYAN + 'Obrigado por jogar ;)')
            break

def verificaPlayer():
    while True:
        jogada = input('Pedra, Papel, ou Tesoura: ').capitalize()
        for i in range(len(jogadas)):
            if jogada == jogadas[i]:
                return jogada
        print(Fore.RED + 'Selecione uma opção correta')

def bot(bot, player):
    if bot == 'Pedra' and player == 'Tesoura': 
        print(Fore.YELLOW + '\nPedra quebra testoura, o BOT ganhou\n')
        return True
    elif bot == 'Papel' and player == 'Pedra': 
        print(Fore.YELLOW + '\nPapel cobre Pedra, o BOT ganhou\n')
        return True
    elif bot == 'Tesoura' and player == 'Papel': 
        print(Fore.YELLOW + '\nTesoura corta Papel, o BOT ganhou\n')
        return True
    return False

def player(bot, player):
    if player == 'Pedra' and bot == 'Tesoura': 
        print(Fore.BLUE + '\nPedra quebra testoura, o Player ganhou\n')
        return True
    elif player == 'Papel' and bot == 'Pedra': 
        print(Fore.BLUE + '\nPapel cobre Pedra, o Player ganhou\n')
        return True
    elif player == 'Tesoura' and bot == 'Papel': 
        print(Fore.BLUE + '\nTesoura corta Papel, o Player ganhou\n')
        return True
    return False

def defineGanhador(bot, player):
    if bot == True and player == False: print(Fore.YELLOW + '\nO BOT ganhou essa rodada\n')
    elif bot == False and player == True: print(Fore.BLUE + '\nO jogador ganhou essa rodada\n')
    else: print(Fore.GREEN + '\nEssa rodada deu empate\n')

comecaJogo()
