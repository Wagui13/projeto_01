
class Relogio:
    def __init__(self):
        self.horas = 23
        self.minutos = 59  
    
    def regressaTempo(self, minutos): # recebe quantos minutos irá diminuir das horas
        self.minutos -= minutos
        if(self.minutos < 0):
            self.horas -=1
            self.minutos = 59      
        return f"Faltam {self.horas:02d}:{self.minutos:02d}h para entregar o projeto"
    
    def tarefaTempo(self): # assim que o cidadão recebe a tarefa se inicia um conômetro reduzindo o tempo
        import time
        while self.horas > 0 or self.minutos > 0: 
            print(f"{self.horas:02d}:{self.minutos:02d}")
            self.regressaTempo(1)
            time.sleep(1)

class Programador:
    def __init__(self, energia, sono):
        self.energia = 10
        self.sono = 0
    
    def energia(self,s):
        if self.energia > 0:
            s = int(input('Digite a energia'))
            self.energia = self.energia + s
"""
    #def __str__(self):

    #def dormir(self):


class trabalho:
    def __init__(self):

    def eventos_trabalho(self):


class casa:
    def __init__(self):

    def eventos_casa(self):
        
class projeto:
"""


def telaInicial():
    import os
    os.system('color 0a')
    print("""
             _______________________________________________
            /                                               \\
           |    _________________________________________    |
           |   |                                         |   |
           |   |  C:\> _                                 |   |
           |   |       _______   _     _   _             |   |
           |   |       \\____/ \\ | \\   / | | |            |   |
           |   |        ____| | | |___| | | |__          |   |
           |   |       /\___\ /  \____/ | | '_ \\         |   |
           |   |      | |_____        | | | | | |        |   |
           | __|__     \\/_____/       \\_| |_| |_|  _     |   |
           ||  _  |___ ___ ___ ___ ___ _____ ___ _| |____|__ |
           ||   __|  _| . | . |  _| .'|     | .'| . | . |  _|| 
           ||__|  |_| |___|_  |_| |__,|_|_|_|__,|___|___|_|  |
           |   |          |___|                          |   |
           |   |                                         |   |
           |   |_________________________________________|   |
           |                                                 |
            \________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'""")