class relogio:
    def __init__(self):
        self.horas = 23
        self.minutos = 59  
    def contagem_regressiva(self):
        return f"faltam{self.horas:02d}:{self.minutos:02d} para entregar o projeto"
    def custo_tempo(self, minutos): #operações maiores que 60 minutos dá erro
        self.minutos -= minutos
        if self.minutos < 0:
            self.horas += self.minutos // 60
            self.minutos = self.minutos + 60
# a = relogio()
# while True:
#     tempo = int(input('Quantos minutos ? '))
#     a.custo_tempo(tempo)
#     print (a.minutos)
#     print (a.horas)
#     def atrasado(self):

class programador:
    def __init__(self, energia, sono):
        self.energia = 10
        self.sono = 0
    
    def energia(self,s):
        if self.energia > 0:
            s = int(input('Digite a energia'))
            self.energia = self.energia + s

        

    #def __str__(self):

    #def dormir(self):


class trabalho:
    def __init__(self):

    def eventos_trabalho(self):


class casa:
    def __init__(self):

    def eventos_casa(self):
        
class projeto:
