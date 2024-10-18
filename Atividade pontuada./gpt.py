def calcular_inss(salario):
    if salario <= 1100:
        inss = salario * 0.075
    elif salario <= 2203.48:
        inss = salario * 0.09
    elif salario <= 3305.22:
        inss = salario * 0.12
    elif salario <= 6433.57:
        inss = salario * 0.14
    else:
        inss = 854.36  # Valor máximo de desconto
    return inss

def calcular_irrf(salario, dependentes):
    # Definindo as faixas do IRRF
    deducao_dependentes = dependentes * 189.59
    if salario <= 2259.20:
        irrf = 0
    elif salario <= 2826.65:
        irrf = (salario * 0.075) - 142.80 - deducao_dependentes
    elif salario <= 3751.05:
        irrf = (salario * 0.15) - 354.80 - deducao_dependentes
    elif salario <= 4664.68:
        irrf = (salario * 0.225) - 636.13 - deducao_dependentes
    else:
        irrf = (salario * 0.275) - 869.36 - deducao_dependentes
    return max(irrf, 0)  # O IRRF não pode ser negativo

def calcular_vale_transporte(salario, deseja_vale):
    if deseja_vale.lower() == 's':
        return salario * 0.06
    return 0

def calcular_vale_refeicao(valor_refeicao):
    return valor_refeicao * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150  # Desconto fixo por dependente

def main():
    print("Bem-vindo ao Sistema de Folha de Pagamento!")

    # Solicita matrícula e senha (validação não implementada, apenas para entrada)
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")

    # Solicita dados do funcionário
    salario = float(input("Informe o salário base (R$): "))
    dependentes = 1  # Considera que o funcionário possui 1 dependente.
    
    # Verifica o vale transporte
    deseja_vale_transporte = input("Você deseja receber vale transporte? (s/n): ")

    # Valor do vale refeição fornecido pela empresa
    valor_vale_refeicao = float(input("Informe o valor do vale refeição (R$): "))

    # Cálculos dos descontos e acréscimos
    inss = calcular_inss(salario)
    irrf = calcular_irrf(salario, dependentes)
    vale_transporte = calcular_vale_transporte(salario, deseja_vale_transporte)
    vale_refeicao = calcular_vale_refeicao(valor_vale_refeicao)
    plano_saude = calcular_plano_saude(dependentes)

    # Cálculo do salário líquido
    salario_bruto = salario
    descontos = inss + irrf + vale_transporte + plano_saude + vale_refeicao
    salario_liquido = salario_bruto - descontos

    # Exibição do resultado
    print(f"\nResumo da Folha de Pagamento:")
    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Desconto INSS: R$ {inss:.2f}")
    print(f"Desconto IRRF: R$ {irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {vale_transporte:.2f}")
    print(f"Desconto Plano de Saúde: R$ {plano_saude:.2f}")
    print(f"Desconto Vale Refeição: R$ {vale_refeicao:.2f}")
    print(f"\nSalário Líquido: R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    main()
