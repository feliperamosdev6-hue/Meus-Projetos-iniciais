# Projeto 1

def linha():
    print("=" * 30)

Certificados_Felipe = ("file:///C:/Users/niste/Downloads/certificado%20fullstack%20(2).pdf")

linha()
print("Olá meu nome é Felipe Ramos e estou buscando a minha primeira oportunidade de ingressar no universo de TI")
linha()

print("Email: feliperamosdev6@gmail.com")
print("Certificados:", Certificados_Felipe)

# Projeto: Sistema de Faturamento — Fixa Prime

import pandas as pd

def titulo(txt):
    print("-" * 50)
    print(txt.center(50))
    print("-" * 50)

dados = [
    ["Boltinox", "Janeiro", 120, 4200.00],
    ["Boltinox", "Fevereiro", 90, 3150.00],
    ["Indufix", "Janeiro", 150, 5000.00],
    ["Indufix", "Fevereiro", 200, 7200.00],
    ["Liderinox", "Janeiro", 80, 2880.00],
    ["Liderinox", "Fevereiro", 130, 4680.00],
    ["ASTM", "Janeiro", 60, 2100.00],
    ["ASTM", "Fevereiro", 75, 2625.00],
]

df = pd.DataFrame(dados, columns=["Empresa", "Mês", "Quantidade", "Valor (R$)"])

titulo("Tabela de Compras Mensais")
print(df)

titulo("Faturamento por Mês")
print(df.groupby("Mês")["Valor (R$)"].sum().reset_index())

titulo("Faturamento por Empresa")
print(df.groupby("Empresa")["Valor (R$)"].sum().reset_index())

titulo("Faturamento Total")
print(f"R$ {df['Valor (R$)'].sum():,.2f}")
