notas = {
 'João': [7, 8, 9],
 'Maria': [10, 9, 8],
 'Ana': [6, 7, 8]
}

media = {aluno: sum(notas) / len(notas)
        for aluno , notas in notas.items()}

print(media)
