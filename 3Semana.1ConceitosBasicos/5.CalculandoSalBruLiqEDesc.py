def calcular_salario_liquido(salario_bruto, desconto_ir):
    if salario_bruto <= 1903.98:
        imposto_renda = 0
    elif salario_bruto <= 2826.65:
        imposto_renda = salario_bruto * 0.075
    elif salario_bruto <= 3751.05:
        imposto_renda = salario_bruto * 0.15
    elif salario_bruto <= 4664.68:
        imposto_renda = salario_bruto * 0.225
    else:
        imposto_renda = salario_bruto * 0.275
    
    salario_liquido = salario_bruto - imposto_renda - desconto_ir
    return salario_liquido

salario_bruto = float(input("Digite o salário bruto: "))
desconto_ir = float(input("Digite o percentual de desconto do Imposto de Renda: "))

salario_liquido = calcular_salario_liquido(salario_bruto, desconto_ir)
print("O salário líquido é:", salario_liquido)