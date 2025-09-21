def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return f"IMC: {imc:.2f} - Bajo peso"
    elif imc < 25:
        return f"IMC: {imc:.2f} - Normal"
    elif imc < 30:
        return f"IMC: {imc:.2f} - Sobrepeso"
    else:
        return f"IMC: {imc:.2f} - Obesidad"