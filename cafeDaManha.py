import modulo_telaInicial

def pedidoFeito(pedido): 
    input(f"""
    +------------------------------------------------------+
                      Pedido realizado - {pedido}         
    +------------------------------------------------------+
                         -> Continuar <-\n{" "*32}""")

def cafeMenu():
    precos = {"Café":4.50, "Pão francês":2.10, "Misto quente":6.35, "Suco":8.99, "Porção de Frutas":15.90, "Omelete": 10.0}
    pedidos = {"Café":0, "Pão francês":0, "Misto quente":0, "Suco":0, "Porção de Frutas":0, "Omelete": 0}
    while True:
        modulo_telaInicial.limparTela()
        op = input("""
                    O que deseja pedir hoje?        
    +------------------------------------------------------+
    | [1] Café   |   [2] Pão francês   |  [3] Misto Quente | 
    +------------------------------------------------------+
    | [4] Suco  |  [5]  Porção de frutas  | [6] Omelete    |
    +------------------------------------------------------+
    |                     [123] Sair                       |
    +------------------------------------------------------+
                            -> """) 

        if op == '1':
            pedidos["Café"] += 1
            pedidoFeito("Café")
        elif op == '2':
            pedidos["Pão francês"] += 1
            pedidoFeito("Pão francês")
        elif op == '3':
            pedidos["Misto quente"] += 1
            pedidoFeito("Misto quente")
        elif op == '4':
            pedidos["Suco"] += 1
            pedidoFeito("Suco")
        elif op == '5':
            pedidos["Porção de Frutas"] += 1
            pedidoFeito("Porção de Frutas")
        elif op == '6':
            pedidos["Omelete"] += 1
            pedidoFeito("Omelete")
        elif op == '123':
            break
        else:
            input(f"""
    +------------------------------------------------------+
    |         Operação inválida! Tente novamente:          |
    +------------------------------------------------------+
                       -> Press enter <-\n{" "*32}""")
    
    # for para mostrar os itens comprados do dicionário
    total = 0
    for c, v in pedidos.items():
        if v > 0:
            print(f"    Pedido: {c} - Qtd: {v}")
            total += precos[c] * pedidos[c]

    input(f"""
    +------------------------------------------------------+
                    Total à pagar: R${total}          
    +------------------------------------------------------+
                       -> Press enter <-\n{" "*32}""")
    
    return int(total) # retorna o total da compra pra subtrair com o valor do personagem