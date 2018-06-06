from pplay.window import *
import game

def inicio(janela):
    mouse = Window.get_mouse()
    janela.set_title('Menu')
    janela.set_background_color((0,0,0))
    while True:
        janela.update()
        if mouse.is_button_pressed(1):
            game.jogo(janela,1)


janela = Window(1100,650)
inicio(janela)
