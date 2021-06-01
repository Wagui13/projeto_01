import modulo_transporte, modulo_trabalho, modulo_telaInicial, cafeDaManha
class Relogio:
    def __init__(self): #horario que o personagem acorda
        self.horas = 6
        self.minutos = 0
    
    def __str__(self): #corrigindo a forma de ler o horario
        return f"\t\t      Relogio: {self.horas:02d}:{self.minutos:02d}"
    
    def avancaTempo(self, minutos): #função para fazer o tempo passar
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

class Programador: #esse são os "atributos" do personagem
    def __init__(self):
        self.energia = 80 
        self.sono = 0
        self.fome = 10
        self.saude = 100
        self.dinheiro = 200
        self.pericia = 1
    
    def __str__(self):
        return modulo_telaInicial.graficoBarras(self.energia, self.sono, self.fome, self.saude, self.dinheiro, self.pericia)
        #return f'Energia: {self.energia:02d}\tFome: {self.sono:02d}\nSono: {self.sono:02d}/10\tSaude: {self.saude}\nDinheiro: {self.dinheiro}\tPericia: {self.pericia}'

    def gastaenergia(self, energia): #função feita para diminuir a "vida" do personagem
        self.energia -= energia

    def sonolento(self, sono=0): #essa função é ativada se a energia baixar muito e acelera o processo de perda de energia, prejudiando até a saude
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
            
    def dfome(self, fome=0): #caso o personagem fique com muita fome el acaba perdendo energia
        self.fome += fome
        if self.fome > 30:
            self.energia -= 1
        elif self.fome >= 50:
            self.fome -= 4
            self.energia -= 2

    def dsaude(self, saude=100): #caso a saude chegue em 40 ele vai perdendo mais energia, se chegar a zero também zera a energia e o jogo acaba
        self.saude += saude
        if self.saude < 40:
            self.energia -=1
        elif self.saude == 0:
            self.energia = 0

    def gastadinheiro(self, dinheiro): #pra dar uma sensação de realidade, mas ainda não tive como colocar validação
        self.dinheiro -= dinheiro

    def ganhapericia(self, pericia): #pericia é a habilidade usada para progredir no projeto, quanto maior a pericia, mais facil ele vai realizar a tarefa
        self.pericia += pericia

class Projeto: #o projeto inicia em zero e finaliza o jogo quando fizer 100
    def __init__(self):
        self.progresso = 0

    def __str__(self):
        return f'\t\t     Projeto:  {self.progresso:02d}/100'

    def trabalharprojeto(self, pericia): #quando ele trabalha no projeto os pontos de pericia vão acumulando progresso até bater ou passar de 100
        self.progresso += pericia

if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    personagem = Programador()
    projeto = Projeto()
    casa = True #se casa for True ativará as opções da casa se for False ativará as opções do trabalho
    senha = False #se a senha for False é porque o personagem ainda não conseguiu preenchela para ligar o computador

modulo_telaInicial.telaInicial()
# aqui vamos apresentar as opções ( troquei as funções por prints para melhorar a lógica enquanto desenvolvemos essas funções)
while casa == True:
        input()
        modulo_telaInicial.limparTela()
        if relogio.horas < 24 and personagem.energia > 0 and personagem.sono < 10 and projeto.progresso <= 100:
            print('-='*30)
            print(relogio)
            print(projeto)
            personagem.sonolento()
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
                personagem.gastadinheiro(cafeDaManha.cafeMenu())
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
            if relogio.horas >= 24:
                print ('Essa não! o prazo se esgotou!')
            elif personagem.energia <= 0:
                print('Essa não! Saude em primeiro luga! você acabou adoecendo e o projeto foi para outra pessoa!')
            elif personagem.sono >=10:
                print('Um carneirinho... Dois carneirinhos... espera aí! você dormiu!')
            elif projeto.progresso >= 100:
                print ('Parabéns! Você entregou o projeto! A promoção é sua!')
            break
while casa == False:
    input()
    modulo_telaInicial.limparTela()
    if relogio.horas < 24 and personagem.energia > 0 and personagem.sono < 10 and projeto.progresso <= 100:
            print('-='*30)
            print(relogio)
            print(projeto)
            personagem.sonolento()
            print(personagem)
            print('-='*30)
            print("Ações No Trabalho:")
            print("1 - Falar com o Chefe")
            print("2 - Ligar o Computador")
            print("3 - Ajudar o Estagiário")
            if senha == True:
                print("4 - Pausa pro café")
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
                personagem.gastaenergia(5)
            elif opcao == "4":
                if personagem.dinheiro > 0:
                    personagem.gastaenergia(modulo_trabalho.cafeteria())
                    personagem.gastadinheiro(5)
                    personagem.dsaude(-1)
                else:
                    print('Você está sem grana!')
                    personagem.gastaenergia(2)
            elif opcao == "5":
                projeto.trabalharprojeto(personagem.pericia)
                personagem.ganhapericia(modulo_trabalho.codar())
                relogio.avancaTempo(30)
                personagem.gastaenergia(10)

            elif opcao == "0":
                print('-+-'*15,'GAME OVER','-+-'*15)
                break
            else:
                print("Opção inválida!")
    else:
        print('-+-'*15,'GAME OVER','-+-'*15)
        if relogio.horas >= 24:
            print ('Essa não! o prazo se esgotou!')
        elif personagem.energia <= 0:
            print('Essa não! Saude em primeiro luga! você acabou adoecendo e o projeto foi para outra pessoa!')
        elif personagem.sono >=10:
            print('Um carneirinho... Dois carneirinhos... espera aí! você dormiu!')
        elif projeto.progresso >= 100:
            print ('Parabéns! Você entregou o projeto! A promoção é sua!')
        break
