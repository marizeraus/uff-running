from pplay.window import *
from pplay.gameimage import *
from pplay.sprite import *


def jogo(janela,fase):
    janela.clear()
    janela = Window(1100,650)
    janela.set_title('UFF Running')
    fundo = GameImage('images/fundo_maior.png')
    fundo_vel = -18
    tempocorrido = 0
    personagem = Sprite('images/character_basic.png', 10)
    personagem.set_position(430,300)
    personagem.set_sequence_time(0,10,120, True)
    personagem.set_final_frame(7)
    keyboard = Window.get_keyboard()
    vel_jump = 2
    pulando = False
    count = 0
    predio1 = GameImage('images/predio_ic.png')
    predio1.set_position(70,50)
    predio2 = GameImage('images/predio_fisica.png')
    predio2.set_position(1200,50)
    predio1_z = False
    predio2_z = False
    parou = False
    tempo_max = 20
    while True:
        fundo.draw()
        personagem.draw()
        if fundo.x>-120:
            predio1.draw()
            predio1_z = True
        else:
            predio2.draw()
            predio2_z = True
        if fundo.x<=-450:
            fundo_vel=0
        else:
            tempocorrido+=janela.delta_time()
            if keyboard.key_pressed('right'):
                personagem.update()
                fundo.x+=fundo_vel*janela.delta_time()
                predio1.x-=38*janela.delta_time()
                if predio2_z:
                    predio2.x-=38*janela.delta_time()
                    if predio2.collided(personagem):
                        fundo.x=-451
                        parou = True
            if pulando:
                personagem.move_y(-vel_jump)
                count+=1
                if count==45:
                    vel_jump=-vel_jump
                    count+=1
                if count==90:
                    personagem.set_position(personagem.x,300)
                    count = 0
                    pulando = False
                    vel_jump = -vel_jump
            if keyboard.key_pressed('space') and count==0:
                pulando=True
        if parou:
            if tempocorrido<tempo_max:
                janela.draw_text('Você chegou a tempo!',janela.height/2,janela.width/2,40,(0,0,0), "Arial", False, False)
            else:
                janela.draw_text('OPS, Você chegou atrasado :(',janela.height/2,janela.width/2,40,(0,0,0), "Arial", False, False)
        else:
            if tempocorrido > tempo_max:
                janela.draw_text('Corra, você está atrasado', 100, janela.width / 2, 40, (0, 0, 0),"Arial", False, False)

        cronometro(tempocorrido, janela,tempo_max)
        janela.update()
        if keyboard.key_pressed('ESC'):
            janela.clear()
            menu.inicio(janela)
def cronometro(tempo, janela, tempo_max):
    tempo2=str(tempo)
    seg,aaa=tempo2.split('.')
    tempo = tempo_max - int(seg)
    if tempo>0:
        janela.draw_text(str(tempo),10,10,40,(0,0,0), "Arial", False, False)
    else:
        janela.draw_text('0',10,10,40,(0,0,0), "Arial", False, False)

def character(itens):
    if itens==0:
        personagem = Sprite('images/character_basic.png', 10)
    return personagem

