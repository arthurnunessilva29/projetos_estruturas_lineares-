import subprocess

subprocess.run("cls",shell=True) 

itens = ("Retirar senha","Chamar próximo aluno","Mostrar Fila","Sair")
fila = []

while True:
    print("Secretaria Acadêmica")
    for i, item in enumerate(itens,start=1):
        print(f"[{i}] - {item}")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            aluno = input('Nome do aluno: ')
            fila.append(aluno)
            print(f'{aluno} entrou na fila de atendimento ')
        
        case '2':
               if len(fila) > 0:
                    atendido = fila.pop(0)
                    print("Chamando Aluno: ", atendido)
        
        case '3':
            if fila:
                print(f"Fila Atual:")
                for i, posicao in enumerate (fila,start=1):
                    print(f'{i} - {posicao}')
            else:
                print('A fila está vazia')
        
        case '4':
            break
        
        case default:
            print ('Insira uma opção válida!!!')
        
      


        
