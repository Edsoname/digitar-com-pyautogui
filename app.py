#como digitar com pyautogui
import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','V')

#remover mouse até campo de digitar
pyautogui.moveTo(1213,720, duration=2)
#clicar no campo de digitar
pyautogui.click()
#digitar minha mensagem
escrever_frase('Oi filha te amo!')
#pyautogui.typewrite('olá bom dia!')
#clicar no botão de enviar
pyautogui.click(1350,715,duration=2)
