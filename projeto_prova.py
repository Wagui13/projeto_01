import modulo_transporte, modulo_trabalho, modulo_telaInicial
class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
    
    def __str__(self):
        return f"\tRelogio:{self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

class Programador:
    def __init__(self):
        self.energia = 80
        self.sono = 0
        self.fome = 10
        self.saude = 100
        self.dinheiro = 1000
        self.pericia = 1
    
    def __str__(self):
        return f'Energia: {self.energia:02d}\tFome: {self.sono:02d}\nSono: {self.sono:02d}/10\tSaude: {self.saude}\nDinheiro: {self.dinheiro}\tPericia: {self.pericia}'

    def gastaenergia(self, energia):
        self.energia -= energia

    def sonolento(self, sono=0): 
        self.sono += sono
        if self.energia < 50:
            self.sono += 1
        elif self.energia < 20:
            self.sono += 2
        elif self.energia >= 51:
            self.sono -= 1
        if self.sono < 0:
            self.sono = 0
        elif self.sono > 3:
            self.saude -= 2
            
    def dfome(self, fome=0):
        self.fome += fome
        if self.fome > 30:
            self.energia -= 1
            self.energia -= 1
        elif self.fome >= 50:
            self.fome -= 4
            self.energia -= 2

    def dsaude(self, saude=100):
        self.saude += saude
        if self.saude < 40:
            self.energia -=1
        elif self.saude == 0:
            self.energia = 0

    def gastadinheiro(self, dinheiro):
        self.dinheiro -= dinheiro

    def ganhapericia(self, pericia):
        self.pericia += pericia

class Projeto:
    def __init__(self):
        self.progresso = 0

if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    personagem = Programador()
    projeto = Projeto()
    casa = True #se casa for True ativará as opções da casa se for False ativará as opções do trabalho
    senha = False

modulo_telaInicial.telaInicial()
# aqui vamos apresentar as opções ( troquei as funções por prints para melhorar a lógica enquanto desenvolvemos essas funções)
while casa == True:
        if relogio.horas < 24 and personagem.energia > 0 and personagem.sono < 10:
            print('-='*30)
            print(relogio)
            #personagem.sonolento()
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
                print('\nVocê tomou banho!') #Esta consome tempo
                relogio.avancaTempo(15)
                personagem.gastaenergia(2)
            elif opcao == "2":
                print('\nFez café da manhã!')#Esta consome tempo e gasta 1 energia
                relogio.avancaTempo(20)
                personagem.gastaenergia(5)
            elif opcao == "3":
                print('\nPediu café da manha')#Esta consome tempo
                relogio.avancaTempo(25)
                personagem.gastaenergia(1)
                personagem.gastadinheiro(15)
            elif opcao == "4":
                print('\nTomou café')#esta consome tempo e dá +2 de energia
                relogio.avancaTempo(20)
                personagem.gastaenergia(-5)
                personagem.dfome(-5)
            elif opcao == "5":
                print('-='*10,'TRANSPORTE','-='*10)
                print('''Você vai trabalhar de:\n1 - Carro\n2 - Ônibus\n3 - Uber\n''')
                opcao2 = input('Escolha seu transporte:')
                if opcao2 == '1':
                    tempo = modulo_transporte.transporte(1)
                    relogio.avancaTempo(tempo)
                    personagem.gastaenergia(10)
                    casa = False
                elif opcao2 == '2':
                    tempo = modulo_transporte.transporte(2)
                    relogio.avancaTempo(tempo)
                    personagem.gastaenergia(20)
                    personagem.gastadinheiro(10)
                    casa = False
                elif opcao2 == '3':
                    tempo = modulo_transporte.transporte(3)
                    relogio.avancaTempo(tempo)
                    personagem.gastaenergia(5)
                    personagem.gastadinheiro(30)
                    casa = False
                else:
                    print('Erro! Escolha um meio de Transporte!')
            elif opcao == "0":
                print('-+-'*15,'GAME OVER','-+-'*15)
                break
            else:
                print("Opção inválida!")
        else:
            print('-+-'*15,'GAME OVER','-+-'*15)
            break
while casa == False:
    if relogio.horas < 24 and personagem.energia > 0 and personagem.sono < 10:
            print('-='*30)
            print(relogio)
            personagem.sonolento()
            print(personagem)
            print('-='*30)
            print("Ações No Trabalho:")
            print("1 - Falar com o Chefe")
            print("2 - Ligar o Computador")
            print("3 - Ajudar o Estagiário")
            if senha == True:
                print("4 - Consultar o Stack Overflow")
                print("5 - Codar! Codar! Codar!")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            if opcao == "1":
                personagem.ganhapericia(modulo_trabalho.falarcomchefe())
                relogio.avancaTempo(15)
                personagem.gastaenergia(5)
            elif opcao == "2":
                if senha != True:
                    senha = modulo_trabalho.senhadopc()
                relogio.avancaTempo(5)
                personagem.gastaenergia(2)
            elif opcao == "3":
                modulo_trabalho.ajudarestagiario()
            elif opcao == "4":
                modulo_trabalho.stackoverflow()
            elif opcao == "5":
                modulo_trabalho.codar()
            elif opcao == "0":
                print('-+-'*15,'GAME OVER','-+-'*15)
                break
            else:
                print("Opção inválida!")
    else:
        print('-+-'*15,'GAME OVER','-+-'*15)
        break
