import matplotlib.pyplot as plt
from situacao import *

df = pd.read_excel('alunos.ifpb.xls')

situacao = pd.crosstab(index=newData["Situação"], columns="Quantidade")
curso = pd.crosstab(index=newData["Curso"], columns="Quantidade")
periodo = pd.crosstab(index=newData["Ano/Periodo Letivo"], columns="Quantidade")

evadidosPorCurso = pd.crosstab(index=evasao["Curso"], columns="Quantidade")

print(evadidosPorCurso)

porcentagem = evadidosPorCurso/evadidosPorCurso.sum()
print(porcentagem, "\n")

# Criando uma lista de rótulos com os nomes das situações
labels = [label[:3] for label in porcentagem.index.tolist()]

# Criando uma lista com os valores (porcentagens) correspondentes
sizes = porcentagem['Quantidade'].values * 100  # Multiplicando por 100 para converter em porcentagem

# Configurando o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 7))  # Aumentando o tamanho da figura

# Criando o gráfico de barras horizontal
ax.barh(labels, sizes, color='skyblue')

# Adicionando os rótulos de porcentagem ao lado de cada barra
for i in range(len(sizes)):
    ax.text(sizes[i] + 1, i, f'{sizes[i]:.1f}%', va='center')

# Configurando título e rótulos dos eixos
ax.set_xlabel('Porcentagem (%)')
ax.set_ylabel('Código do curso')
ax.set_title('Distribuição dos alunos evadidos por curso')

# Ajustando automaticamente o layout para que os rótulos não sejam cortados
plt.tight_layout()

# Exibindo o gráfico gerado
plt.show()