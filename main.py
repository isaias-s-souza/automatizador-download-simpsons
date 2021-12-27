import pyautogui as robo
import time

robo.alert('A automação vai começar')
robo.PAUSE = 1.25
# Abre o Edge
robo.press('win')
robo.write('edge')
robo.press('enter')
time.sleep(2)
# Percorre Todos Episódios
for numEpisodio in range(1, 619):
    templateURL = 'https://assistiranimeonline.net/'\
                  'video/os-simpsons-{}-online/'
    robo.write(templateURL.format(str(numEpisodio)))
    robo.press('enter')
    robo.moveTo(760, 635)
    time.sleep(3)
    robo.click()
    # Clica no botão de download
    robo.PAUSE = 0.25
    robo.moveTo(1067, 851)
    robo.moveTo(1067, 852)
    robo.click()
    robo.PAUSE = 1
    time.sleep(30)
    # Abre uma nova aba
    robo.hotkey('ctrl', 't')
    # Volta na aba anterior
    robo.hotkey('ctrl', 'tab')
    # Fecha aba
    robo.hotkey('ctrl', 'w')


