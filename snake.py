from random import randint
from pytimedinput import timedInput
from colorama import Fore, init
import os

#Configurações
LARGURA_CAMPO = 32
ALTURA_CAMPO = 16
CELLS = [(col,row) for row in range(ALTURA_CAMPO) for col in range(LARGURA_CAMPO)]

#print(CELL)
def gerar_mapa():
    global colisao
    print("Pontos = " + str(len(cobra) -3 ))
    for cell in CELLS:
        if cell[0] in (0, LARGURA_CAMPO-1) or cell[1] in (0, ALTURA_CAMPO-1):
            print('#', end = '')
        elif cell in cobra:
            if cell == cobra[0]:
                print(Fore.GREEN + CABECA[direcao], end='')
            elif cell in pos_maca_anterior:
                print(Fore.YELLOW + 'O',end= '')
            else:
                print(Fore.GREEN + 'X', end='')
        elif cell == pos_maca:
            print(Fore.RED + 'M', end='')
        else:
            print(' ', end='')
        if(cell[0] == LARGURA_CAMPO - 1):
            print("")
        
def gerar_maca():
    global pos_maca, pos_maca_anterior
    pos_maca = (randint(1,LARGURA_CAMPO-2),randint(1,ALTURA_CAMPO-2))
    while pos_maca in cobra:
        pos_maca = (randint(1,LARGURA_CAMPO-2),randint(1,ALTURA_CAMPO-2))
    #if pos_maca_anterior[0] == (0,0):
    #    pos_maca_anterior.pop(-1)

def mover_cobra():
    global cresce
    cabeca = (cobra[0][0] + DIRECOES[direcao][0], cobra[0][1] + DIRECOES[direcao][1])
    checa_colisoes(cabeca)
    cobra.insert(0,cabeca)
    if cresce > 0 and pos_maca_anterior[-1] == cobra[-1]:
        cresce -= 1
        pos_maca_anterior.pop(-1)
    else:
        cobra.pop(-1)

def checa_colisoes(cabeca):
    global pos_maca_anterior, cresce, colisao
    if cabeca in cobra or cabeca[0] in (0,LARGURA_CAMPO-1) or cabeca[1] in (0,ALTURA_CAMPO - 1):
        colisao = True
    if cabeca == pos_maca:
        pos_maca_anterior.insert(0,pos_maca)
        cresce +=1
        gerar_maca()

#Gerar Cobra:
cobra = [(LARGURA_CAMPO/2, ALTURA_CAMPO/2),(LARGURA_CAMPO/2 - 1, ALTURA_CAMPO/2),(LARGURA_CAMPO/2 - 2, ALTURA_CAMPO/2)]
CABECA = {"W": 'A', "S": 'V', "A": '<', "D": '>'}
cresce = 0
colisao = False

#Movimento da cobra:
DIRECOES = {"W": (0,-1), "S": (0,1), "A": (-1,0), "D": (1,0)}
direcao = 'D'

#Gerar maçã:
pos_maca_anterior = []
gerar_maca();

init(autoreset=True)

while True:
    #Limpa o terminal:
    #os.system("\033[H")
    os.system("\033[H")

    #Movimento da cobra:
    mover_cobra()

    #Atualizar o mapa:
    gerar_mapa();

    #Recebe o comandp:
    txt,_ = timedInput('Get input: ', timeout=0.2)
    if txt in ('w','a','s','d'):
        direcao = txt.upper();
    elif txt == 'q':
        os.system('cls')
        break
    #Checa se o jogo acabou:
    if colisao:
        os.system('cls')
        break

print("Pontuacao Final = " + str(len(cobra) -3 ))

