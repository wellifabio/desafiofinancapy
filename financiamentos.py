import pandas as pd
import matplotlib.pyplot as plt

#Ler dados, valor financiado, taxa de juros e número de parcelas
print("Digite o valor financiado:")
valor_financiado = float(input())
print("Digite a taxa de juros:")
taxa_juros = float(input())
print("Digite o número de parcelas:")
num_parcelas = int(input())

#Cálculo do valor da parcela M = P(1 + i)^n / n
valor_parcela = valor_financiado * (1 + taxa_juros/100)**num_parcelas / num_parcelas

print("O valor da parcela é: ", valor_parcela)

# criando um vetor com os meses
meses = []
for i in range(num_parcelas):
    meses.append(i+1)

# criando um vetor com os valores das parcelas
saldo_devedor = valor_financiado
parcelas = []
juross = []
saldos = []
for i in range(num_parcelas):
    amortizacao = valor_financiado / num_parcelas
    juros = saldo_devedor * taxa_juros / 100
    prestacao = amortizacao + juros
    juross.append(juros)
    parcelas.append(prestacao)
    saldos.append(saldo_devedor)
    saldo_devedor -= amortizacao

#mostrar tabela com os meses e valores das parcelas com duas casas decimais
print("Mes,Parcela,Juros,Saldo")
for i in range(num_parcelas):
    print(meses[i], ",", round(parcelas[i], 2), ",", round(juross[i], 2), ",", round(saldos[i], 2))

#criação do gráfico
df = pd.DataFrame({'mes': meses, 'parcela': parcelas})
df.plot(x='mes', y='parcela', kind='bar')
plt.title('Parcelas por mês')

#Configuração do gráfico
plt.title('Parcelas por mês')
#remover bordas do gráfico
plt.gca().spines['top'].set_visible(False)
#remover borda da direita
plt.gca().spines['right'].set_visible(False)
#remover legenda
plt.gca().get_legend().remove()
#Congigurar rotulo valor do eixo x
plt.xlabel('Meses')
#Configuração do eixo y
plt.ylim(parcelas[-1], parcelas[0])


#adicionar rotulo valor do eixo X sobre as barras e colorir de vermelho
for i in range(num_parcelas):
    plt.text(i, parcelas[i], round(parcelas[i], 2), ha = 'center')
    plt.gca().get_children()[i].set_color('red')

#exibição do gráfico
plt.show()

