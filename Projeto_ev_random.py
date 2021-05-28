import random
#Simulando a função de tempo.
tempo = 1500 # Contando q ele entra as 7h no trabalho e começa o projeto as 8h. Tempo em minutos.
dinheiro = 100 #Imaginando que o programador vai ter algum dinheiro na carteira. Se utilizarmos o dinheiro tem que acrescentar validações no código.
tipo_transporte = int(input("Selecione o tipo de transporte que deseja ir ao trabalho hoje.\n[1] Carro [2] Ônibus [3] Uber: "))

if tipo_transporte == 1 :
    num_aleatorio = random.randint(0,100)  
    if num_aleatorio >=0 and num_aleatorio < 15 :
        print("Infelizmente seu carro quebrou! Ele terá que ser guinchado.\nEscolha outro transporte para acabar de chegar ao trabalho.")
        escolha = int(input("Qual transporte deseja utilizar: [1] Ônibus. [2] Uber?")) #Não vou colocar nenhuma validaçao por enquanto.
        if escolha == 1 :
            print("Você levará mais 20 minutos para chegar ao trabalho")
            tempo -= 20   # A questão do tempo perdido vcs também podem definir mais ou menos...
            dinheiro -= 70
        else :
            print("Você levará mais 10 minutos para chegar ao trabalho")
            tempo -= 10
            dinheiro -= 80   #Pensei em colocar a cada perda de tempo o status do restante de tempo.
        
    elif num_aleatorio >=15 and num_aleatorio < 30 :
        print("Infelizmente seu carro está com o pneu furado. O que você vai fazer?")
        escolha = int(input("Qual opção: [1] Trocar pneu. [2] Ir até a borracharia mais próxima: "))
        if escolha == 1 :
            print("Você levará mais 30 minutos para chegar ao trabalho")
            tempo -= 30   # A questão do tempo perdido vcs também podem definir mais ou menos...
        else :
            print("Você levará mais 70 minutos para chegar ao trabalho")
            tempo -= 70
            dinheiro -= 30

    elif num_aleatorio >= 30 and num_aleatorio < 45 :
        print("Inacreditável!!! Você teve seu carro roubado e deverá realizar um boletim de ocorrência antes de ir ao trabalho.")
        escolha = int(input("Com a ocorrência feita digite a opção para chegar ao trabalho: [1] Ir de ônibus. [2] Ir de Uber: "))
        if escolha == 1 :
            print ("Você levará mais 45 minutos para chegar ao trabalho")
            tempo -= 45
            dinheiro -= 10
        else:
            print("Você levará mais 20 minutos para chegar ao trabalho")
            tempo -= 20
            dinheiro -= 20

    elif num_aleatorio >= 45 and num_aleatorio < 60 : # Aqui eu validei dinheiro para termos uma noção.
        print("Você se esqueceu de abastecer seu carro e agora está parado. Por sorte havia um posto na região.")
        if dinheiro >= 50:
            print("Você tem dinheiro suficiente para abastecer e seguir em frente.")
            dinheiro -= 50
            tempo -= 40
        else :
            print("Você não tem dinheiro suficiente para abastecer. Escolha outra opção de transporte:")
            escolha = int(input("[1] Ônibus. [2] Uber: "))
            if escolha == 1 :
                print ("Você levará mais 30 minutos para chegar ao trabalho")
                tempo -= 30
                dinheiro -= 10
            else:
                print("Você levará mais 15 minutos para chegar ao trabalho")
                tempo -= 15
                dinheiro -= 20
    
    else :
        print("Está tudo correndo bem, sem imprevistos. Hoje será seu grande dia!!!")

elif tipo_transporte == 2 :
    num_aleatorio = random.randint(0,100)    
    if num_aleatorio >=0 and num_aleatorio < 15 :
        escolha = input("Infelizmente o ônibus quebrou! Você terá que esperar outro ônibus.\nVocê quer completar o trajeto de Uber? [S] ou [N]: ").upper()
        if escolha == "S" :
            print("Você levará mais 10 minutos para chegar ao trabalho")
            tempo -= 10   
            dinheiro -= 15
        else :
            print("Você levará mais 30 minutos para chegar ao trabalho")
            tempo -= 30
            dinheiro -= 10

    elif num_aleatorio >= 15 and num_aleatorio < 30 :
        print("Justo hoje o ônibus atrasou. Você perderá minutos preciosos para chegar ao trabalho.")
        tempo -= 40
    
    elif num_aleatorio >= 30 and num_aleatorio < 30 :
        print("Você estava tão empolgado com o dia de hoje que pegou o ônibus errado. Agora desça e pegue o ônibus correto.")
        tempo -= 45
    else :
        print("Está tudo correndo bem, sem imprevistos. Hoje será seu grande dia!!!")       

else :
    num_aleatorio = random.randint(0,100)    
    if num_aleatorio >=0 and num_aleatorio < 15 :
        print("Infelizmente o carro do Uber quebrou! Escolha outro transporte para acabar de chegar ao trabalho.")
        escolha = int(input("Qual transporte deseja utilizar: [1] Ônibus. [2] Uber?")) 
        if escolha == 1 :
            print("Você levará mais 20 minutos para chegar ao trabalho")
            tempo -= 20   
            dinheiro -= 10
        else :
            print("Você levará mais 10 minutos para chegar ao trabalho")
            tempo -= 10
            dinheiro -= 40  
      
    elif num_aleatorio >=15 and num_aleatorio < 30 :
        print("Um imprevisto aconteceu: o Uber está com o pneu furado.\n O motorista irá realizar a troca. ")
        tempo -= 40            
        
    elif num_aleatorio >= 30 and num_aleatorio < 45 :
        print("Seu Uber está atrasado. O que pretende fazer?")
        escolha = int(input("Digite a opção desejada: [1] Ir de carro. [2] Ir de ônibus. [3] Chamar outro Uber: "))
        if escolha == 1 :
            print ("Você levará mais 15 minutos para chegar ao trabalho.")
            tempo -= 15
            dinheiro -= 10
        elif escolha == 2 :
            print("Você levará mais 40 minutos para chegar ao trabalho.")
            tempo -= 40
            dinheiro -= 10
        else:
            print("Você levará mais 20 minutos para chegar ao trabalho")
            tempo -= 40
            dinheiro -= 20
    
    else :
        print("Está tudo correndo bem, sem imprevistos. Hoje será seu grande dia!!!")


