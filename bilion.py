import sys
import time

# DESABILITA O LIMITE DE CONVERSÃO DE INTEIRO PARA STRING
sys.set_int_max_str_digits(0)

# ===== CONFIGURAÇÃO =====
n = 5644   # Mude aqui o expoente que deseja
# 9.999.999 Abre de boas
# 99.999.999 Travadinha (e não abre)
# ===== NÚMERO ESCOLHIDO =====
numero_escolhido = 2
# ===== CÁLCULO =====
print(f"Calculando {numero_escolhido}^{n}...")
inicio = time.time()

valor = numero_escolhido ** n

fim = time.time()
digitos = len(str(valor))   # agora funciona sem erro

print(f"Dígitos: {digitos}")
print(f"Tempo de cálculo: {fim - inicio:.2f} segundos")

# ===== EXIBIÇÃO OU SALVAMENTO =====
if digitos <= 100000:
    print(f"Valor:\n{valor}")
else:
    nome_arquivo = f"2_{n}.txt"
    with open(nome_arquivo, "w") as f:
        f.write(str(valor))
    print(f"Número muito grande – salvo em '{nome_arquivo}'") 
    