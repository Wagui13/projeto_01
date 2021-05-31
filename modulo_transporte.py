def transporte(tipo_transporte):
    import random 
    num_aleatorio = random.randint(0,100)
    if tipo_transporte == 1 :
        carro = 20
        if num_aleatorio >=0 and num_aleatorio < 15 :
            print("Infelizmente seu carro quebrou! Ele terá que ser guinchado.\nEscolha outro transporte para acabar de chegar ao trabalho.")
            escolha = int(input("Qual transporte deseja utilizar: [1] Ônibus. [2] Uber?")) #Não vou colocar nenhuma validaçao por enquanto.
            if escolha == 1 :
                print("Você levará mais 30 minutos para chegar ao trabalho")
                return carro+30
            else :
                print("Você levará mais 25 minutos para chegar ao trabalho")
                return carro+25
                #dinheiro -= 80   #Pensei em colocar a cada perda de tempo o status do restante de tempo.
            
        elif num_aleatorio >=15 and num_aleatorio < 30 :
            print("Infelizmente seu carro está com o pneu furado. O que você vai fazer?")
            escolha = int(input("Qual opção: [1] Trocar pneu. [2] Ir até a borracharia mais próxima: "))
            if escolha == 1 :
                print("Você levará mais 30 minutos para chegar ao trabalho")
                return carro+30   # A questão do tempo perdido vcs também podem definir mais ou menos...
            else :
                print("Você levará mais 70 minutos para chegar ao trabalho")
                return carro+70
                #dinheiro -= 30

        elif num_aleatorio >= 30 and num_aleatorio < 45 :
            print("Inacreditável!!! Você teve seu carro roubado e deverá realizar um boletim de ocorrência antes de ir ao trabalho.")
            escolha = int(input("Com a ocorrência feita digite a opção para chegar ao trabalho: [1] Ir de ônibus. [2] Ir de Uber: "))
            if escolha == 1 :
                print ("Você levará mais 95 minutos para chegar ao trabalho")
                return carro+95
                #dinheiro -= 10
            else:
                print("Você levará mais 75 minutos para chegar ao trabalho")
                return carro+75
                #dinheiro -= 20

        # elif num_aleatorio >= 45 and num_aleatorio < 60 : # Aqui eu validei dinheiro para termos uma noção.
        #     print("Você se esqueceu de abastecer seu carro e agora está parado. Por sorte havia um posto na região.")
        #     if dinheiro >= 50:
        #         print("Você tem dinheiro suficiente para abastecer e seguir em frente.")
        #         dinheiro -= 50
        #         tempo -= 40
        #     else :
        #         print("Você não tem dinheiro suficiente para abastecer. Escolha outra opção de transporte:")
        #         escolha = int(input("[1] Ônibus. [2] Uber: "))
        #         if escolha == 1 :
        #             print ("Você levará mais 30 minutos para chegar ao trabalho")
        #             tempo -= 30
        #             dinheiro -= 10
        #         else:
        #             print("Você levará mais 15 minutos para chegar ao trabalho")
        #             tempo -= 15
        #             dinheiro -= 20
        
        else:
            print("Está tudo correndo bem, sem imprevistos. Hoje será seu grande dia!!!")
            return 20

    elif tipo_transporte == 2 :
        onibus = 30
        num_aleatorio = random.randint(0,100)    
        if num_aleatorio >=0 and num_aleatorio < 15 :
            escolha = input("Infelizmente o ônibus quebrou! Você terá que esperar outro ônibus.\nVocê quer completar o trajeto de Uber? [S] ou [N]: ").upper()
            if escolha == "S" :
                print("Você levará mais 25 minutos para chegar ao trabalho")
                return onibus+25   
                #dinheiro -= 15
            else :
                print("Você levará mais 30 minutos para chegar ao trabalho")
                return onibus+30
                #dinheiro -= 10

        elif num_aleatorio >= 15 and num_aleatorio < 30 :
            print("Justo hoje o ônibus atrasou. Você perderá minutos preciosos para chegar ao trabalho.")
            return onibus+40
        
        elif num_aleatorio >= 30 and num_aleatorio < 30 :
            print("Você estava tão empolgado com o dia de hoje que pegou o ônibus errado. Agora desça e pegue o ônibus correto.")
            return onibus+45
        else :
            print("Está tudo correndo bem, sem imprevistos. Hoje será seu grande dia!!!")
            return onibus       

    else :
        uber = 25
        num_aleatorio = random.randint(0,100)    
        if num_aleatorio >=0 and num_aleatorio < 15 :
            print("Infelizmente o carro do Uber quebrou! Escolha outro transporte para acabar de chegar ao trabalho.")
            escolha = int(input("Qual transporte deseja utilizar: [1] Ônibus. [2] Uber?")) 
            if escolha == 1 :
                print("Você levará mais 20 minutos para chegar ao trabalho")
                return uber+20   
                #dinheiro -= 10
            else :
                print("Você levará mais 10 minutos para chegar ao trabalho")
                return uber+10
                #dinheiro -= 40  
        
        elif num_aleatorio >=15 and num_aleatorio < 30 :
            print("Um imprevisto aconteceu: o Uber está com o pneu furado.\n O motorista irá realizar a troca. ")
            return uber+40            
            
        elif num_aleatorio >= 30 and num_aleatorio < 45 :
            print("Seu Uber está atrasado. O que pretende fazer?")
            escolha = int(input("Digite a opção desejada: [1] Ir de carro. [2] Ir de ônibus. [3] Chamar outro Uber: "))
            if escolha == 1 :
                print ("Você levará mais 15 minutos para chegar ao trabalho.")
                return uber+15
                #dinheiro -= 10
            elif escolha == 2 :
                print("Você levará mais 40 minutos para chegar ao trabalho.")
                return uber+40
                #dinheiro -= 10
            else:
                print("Você levará mais 20 minutos para chegar ao trabalho")
                return uber+40
                #dinheiro -= 20
        
        else :
            print("Está tudo correndo bem, sem imprevistos. Hoje será seu grande dia!!!")
            return uber
