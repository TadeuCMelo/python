#Projeto: Gestor de Inventário do Laboratório de Informática
#Autor: Tadeu Cordeiro Melo
#data: 28/09/2026

salas = ('LAB1','LAB2','LAB3')
estados = ('Operacional','Avariado','Em Reparação')

tipos = ['computador', 'monitor', 'impressora', 'router', 'switch', 'projetor']

inventario = {
    'PC01': {
        'nome': 'desktop hp elitedesk',
        'tipo': tipos[0],
        'sala': salas[0],
        'quantidade': 12,
        'estado': estados[0],
    },
   'Monitor01': {
        'nome': 'monitor 144HZ',
        'tipo': tipos[1],
        'sala': salas[1],
        'quantidade': 12,
        'estado': estados[0],
    },
    'IMP01': {
        'nome': 'impressora lg',
        'tipo': tipos[2],
        'sala': salas[1],
        'quantidade': 1,
        'estado': estados[1],
    },
    'router': {
        'nome': 'Wefe',
        'tipo': tipos[3],
        'sala': salas[2],
        'quantidade': 1,
        'estado': estados[0],
    },
    'switch': {
        'nome': 'switch 3000',
        'tipo': tipos[4],
        'sala': salas[2],
        'quantidade': 1,
        'estado': estados[2],
    },
    'projetor01':{
        'nome': 'Projetor LG',
        'tipo': tipos[5],
        'sala': salas[0],
        'quantidade': 1,
        'estado': estados[1],
    },
}

print(tipos[0])

reparados = []
historico = []

ativo = True

while ativo: 
    mensagem1 = ("================ GESTOR DE INVENTÁRIOS ================")
    mensagem1 += ("\n1 - Listar Equipamentos")
    mensagem1 += ("\n2 - Adicionar Equipamento")
    mensagem1 += ("\n3 - Pesquisar Equipamento")
    mensagem1 += ("\n4 - Alterar estado de um Equipamento")
    mensagem1 += ("\n5 - Remover Equipamento")
    mensagem1 += ("\n6 - Lista de Reparação")
    mensagem1 += ("\n7 - Estatísticas")
    mensagem1 += ("\n8 - Histórico de Operações")
    mensagem1 += ("\n0 - Sair")

    print(mensagem1)
    pergunta = int(input("Escolha uma opção: "))
    if pergunta == 0:
        pergunta2 = input("Deseja mesmo sair?(s/n)")

        if pergunta2 == 's':
            ativo = False
        else:
            continue
    elif pergunta == 1:
         print(f"{'Código':<15} {'Nome':<30} {'Sala':<5} {'Quantidade':<11} {'Estado':<18}")
         print("-" * 79)
         texto_final = "\n".join(
            f"{num:<10} {info['nome'].title():<25} {info['sala']:<10} "
            f"{info['quantidade']:<10} {info['estado']:<18}"
            for num, info in inventario.items()
         )
         print(texto_final)
         conta_inventario = len(inventario)
         if conta_inventario == 0:
             print("O inventário está vazio")
         else:
             print(f"Total de Registos: {conta_inventario}")

         input("Toque enter para continuar")
             
    elif pergunta == 2:
        while True:
            codigo = input("Código do equipamento: ").strip().upper()

            if not codigo:
                print("Precisas escrever algo no código")
                continue

            if codigo in inventario:
                print("Esse código já existe no inventário")
                break

            while True:
                nome = input("Nome do Equipamento: ").strip()
                if not nome:
                    print("Precisas escrever algo no nome.")
                    continue
                break
                

            while True:
                tipo = input(f"Qual o tipo do equipamento ({(tipos)}): ").strip().lower()
                if not tipo:
                    print("O tipo não pode ficar vazio.")
                    continue
                if tipo not in tipos:
                    print(f"O tipo '{tipo}' não é válido. Escolha um da lista.")
                    continue
                break

            sala_valido = True
            while sala_valido:
                print("Salas disponíveis:", salas)
                sala = input("Qual a Sala a que pertence: ").upper()
            
                if sala == "":
                    print("A sala não pode ficar vazia")
                elif sala not in salas:
                    print("A sala não existe. Escolha uma da lista.")
                else:
                    sala_valido = False

            quantidade_valida = True
            while quantidade_valida:
                qnt_input = input("Quantos equipamentos tem?: ")
            
                if qnt_input == "":
                    print("A quantidade não pode ficar vazia")
                else:
                    quantidade = int(qnt_input)
                if quantidade <= 0:
                    print("A quantidade não pode ser igual ou menor que 0")
                else:
                    quantidade_valida = False
            
                break

            break
