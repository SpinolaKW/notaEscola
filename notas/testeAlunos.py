aprovados = []
reprovados = []
final = []

quant_alunos = int(input("Digite a quantidade de alunos da turma: "))

def avaliaSituacaoAluno():
    media = (float(nota1) + float(nota2)) / int(2)
    if media >= 7:
        aprovados.append(nome)
        print(nome, media, " - Aprovado")
    else:
        nota_minima_final = int((50 - (media * 6))) / int(2)
        if nota_minima_final >= 10:
            reprovados.append(nome)
            print(nome, media, " - Reprovado")
        else: 
            final.append(nome)
            print(nome, media, " - Final")

def imprimeSaida():
    print("\n Aprovados: ")
    for aluno in aprovados:
        print(aluno, )
    print("\n Reprovados: ")
    for aluno in reprovados:
        print(aluno, )
    print("\n Final: ")
    for aluno in final:
        print(aluno, )

for iteracao in range(quant_alunos):
    nome = input("\n Nome aluno: ")
    nota1 = input("Nota Prova 1: ")
    nota2 = input("Nota Prova 2: ")
    avaliaSituacaoAluno()

imprimeSaida()