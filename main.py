import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('alunos.ifpb.xls')

# Coletando somente as colunas Curso (3), Situação (4) e Ano/Período Letivo (6)
newData = df[df.columns[[3, 4, 6]]]

# Filtrando os dados por situação, criando subconjuntos para cada situação específica dos alunos
afastado = newData[newData.Situação == 'Afastado']
aguardandoColacao = newData[newData.Situação == 'Aguardando Colação de Grau']
aguardandoENADE = newData[newData.Situação == 'Aguardando ENADE']
cancelado = newData[newData.Situação == 'Cancelado']
cancelamentoCompulsorio = newData[newData.Situação == 'Cancelamento']
concludente = newData[newData.Situação == 'Concludente']
concluido = newData[newData.Situação == 'Concluído']
egresso = newData[newData.Situação == 'Egresso']
estagiarioConcludente = newData[newData.Situação == 'Estagiario (Concludente)']
evasao = newData[newData.Situação == 'Evasão']
falecido = newData[newData.Situação == 'Falecido']
formado = newData[newData.Situação == 'Formado']
intercambio = newData[newData.Situação == 'Intercâmbio']
matriculado = newData[newData.Situação == 'Matriculado']
trancado = newData[newData.Situação == 'Trancado']
trancadoVoluntariamente = newData[newData.Situação == 'Trancado Voluntariamente']
transferidoExterno = newData[newData.Situação == 'Transferido Externo']

# Gerando uma tabela cruzada (crosstab) que conta a quantidade de alunos para cada Situação
situacao = pd.crosstab(index=newData["Situação"], columns="Quantidade")

# Calculando a porcentagem de cada situação em relação ao total
porcentagem = situacao/situacao.sum()
print(porcentagem, "\n")

# print(porcentagem[porcentagem.columns[0]].ix[0])

# a = situacao.rownames
# print(a)

# Criando uma lista de rótulos com os nomes das situações
labels = porcentagem.index.tolist()

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
ax.set_ylabel('Situação')
ax.set_title('Distribuição das Situações dos Alunos')

# Ajustando automaticamente o layout para que os rótulos não sejam cortados
plt.tight_layout()

# Exibindo o gráfico gerado
plt.show()