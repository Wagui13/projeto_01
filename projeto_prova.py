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


# class Trabalho:
#     def __init__(self):

#     def eventos_trabalho(self):


# class Casa:
#     def __init__(self):

#     def eventos_casa(self):
        
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

class Projeto:
    def __init__(self):
        self.progresso = 0

if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    personagem = Programador()
    projeto = Projeto()
    cafe_da_manha = False
#Intro
print('\n'*20)
print('-='*30)
print('\t\tBem Vindo(a) Ao Dev Life')
print('-='*30)
print('''
Você é um jovem programador e o seu superior te deu a oportunidade que você estava esperando!
Você precisa entregar um projeto SUPER importante e tem apenas 24:00 horas para isso!
Entregue o projeto e conquiste sua promoção!
''')
# aqui vamos apresentar as opções ( troquei as funções por prints para melhorar a lógica enquanto desenvolvemos essas funções)
while True:
        if relogio.horas < 24 and personagem.energia > 0 and projeto.progresso <=100:
            print('-='*30)
            print(relogio)
            print(personagem)
            print('-='*30)
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Fazer café da manhã")
            print("3 - Pedir café da manhã")
            print("4 - Tomar café da manhã")
            print("5 - Ir trabalhar")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            if opcao == "1":
                print('Você tomou banho!') #Esta consome tempo
                relogio.avancaTempo(20)
                personagem.gastaenergia(1)
            elif opcao == "2":
                print('Fez café da manhã!')#Esta consome tempo e gasta 1 energia
                relogio.avancaTempo(20)
                personagem.gastaenergia(1)
            elif opcao == "3":
                print('Pediu café da manha')#Esta consome tempo
                relogio.avancaTempo(15)
            elif opcao == "4":
                print('Tomou café')#esta consome tempo e dá +2 de energia
                relogio.avancaTempo(20)
                personagem.gastaenergia(-2)
            elif opcao == "5":
                print('''
                Você vai trabalhar de:
                1 - Carro
                2 - Ônibus
                3 - Uber
                ''')
                opcao2 = input('Escolha seu transporte:')
                if opcao2 == '1':
                    print('Carro') #aqui podemos inserir um random com falha/normal/sorte
                elif opcao2 == '2':
                    print('Ônibus') #aqui podemos inserir um random com falha/normal/sorte
                elif opcao2 == '3':
                    print('Uber') #aqui podemos inserir um random com falha/normal/sorte
                else:
                    print('Erro')
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")
        else:
            break
