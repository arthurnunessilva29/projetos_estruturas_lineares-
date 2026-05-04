import subprocess
subprocess.run('cls', shell=True)

ana = 0
bruno = 0
carlos = 0

print('Candidatos:\n 1. Ana\n 2. Bruno\n 3. Carlos')

while True:
    voto_do_aluno = input('Digite o canditato (fim para encerrar): ').capitalize()
    if voto_do_aluno == 'Ana':
        ana += 1
   
    elif voto_do_aluno == 'Bruno':
        bruno += 1
   
    elif voto_do_aluno == 'Carlos':
        carlos += 1
   
    elif voto_do_aluno == 'Fim':
        break
    else:
        print ('Seu voto é inválido!!!')

print ('Resultados da votação') 
print(f'\nTotais: Ana: {ana}\n Bruno: {bruno}\n Carlos: {carlos}')

if ana > bruno and carlos:
    print('Ana venceu!')
elif bruno > ana and carlos:
    print('Bruno venceu!')
elif carlos > bruno and ana:
    print ('Carlos venceu!')
else:
    print('Houve um empate entre os Candidatos.')