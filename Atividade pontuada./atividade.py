import os
import dataclass
os.system("cls || clear")

#class
@dataclass
class Funcionario:
    nome:str
    idade:int
    cpf:int
    sexo:str
    salario:float
    
#Listas
lista_folha_pagamento=[]
lista_funcionario=[]

#Inicio do inferno
while True:
    for i in range(1):
        funcionarios=Funcionario(
            nome=input("Digite o seu nome:"),
            idade=int(input("Digite sua idade:")),
            cpf=int(input("Digite seu CPF:"))
            sexo=input("Digite seu sexo:")
            salario=float(input("Digite seu salário:"))
        )
        lista_folha_pagamento.append(funcionarios)
    
    