import csv
import json

treinos = []

def criar_sessao(dia, treino):
    sessão = {
        'dia': dia,
        'treino': treino,
        'exercicios': []
    }
    treinos.append(sessão)
    return sessão

def inserir_exercicio(sessao, nome_exercicio):
    novo_exercicio = {
        'nome': nome_exercicio,
        'series': []
    }
    sessao['exercicios'].append(novo_exercicio)
    return novo_exercicio

def adicionar_serie(exercicio, carga, reps):
    serie = {
        'carga': int(carga),
        'reps': int(reps)
    }
    exercicio['series'].append(serie)
    return serie

def mostrar_treino():
    for sessao in treinos:
        print(f"\n{sessao['dia']} | Treino {sessao['treino']}")
        for ex in sessao['exercicios']:
            print(f"\n{ex['nome']}")
            for idx, s in enumerate(ex['series'], start=1):
                print(f"\nSérie {idx}: {s['carga']} x {s['reps']} reps")


if __name__ == '__main__':
    qtde_treinos = int(input('Quantidade de treinos: '))
    for i in range(1, qtde_treinos+1):
        dia_treino = input(f'Dia do treino {i} (formato: YYYY-MM-DD): ')
        tipo_treino = input('Tipo de treino, A, B: ')
        novo_treino = criar_sessao(dia_treino, tipo_treino)
        qtde_exercicios = int(input('Quantidade de exercícios: '))
        for i in range(1, qtde_exercicios+1):
            nome = input(f'Digite o nome do exercício {i}: ')
            exercicio_treino = inserir_exercicio(novo_treino, nome)
            num_series = int(input('Quantidade de séries: '))
            for s in range(1, num_series+1):
                peso = input(f'Carga Série {s} (kg): ')
                repeticoes = input('Repetições: ')
                adicionar_serie(exercicio_treino, peso, repeticoes)
    mostrar_treino()
