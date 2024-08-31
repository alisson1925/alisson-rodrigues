string = input("Digite a string que deseja inverter: ")  # Ou use string = "sua string aqui"
inversa = ""
for i in range(len(string) - 1, -1, -1):
    inversa += string[i]
print(f"String invertida: {inversa}")
