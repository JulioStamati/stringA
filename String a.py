# Função para verificar a existência da letra 'a' e contar quantas vezes ela aparece
def verificar_letra_a(string):
    # Convertendo a string para minúsculas para facilitar a contagem
    string_lower = string.lower()
    
    # Contando quantas vezes a letra 'a' aparece
    count_a = string_lower.count('a')
    
    # Verificando se a letra 'a' existe e retornando o resultado
    if count_a > 0:
        return f"A letra 'a' aparece {count_a} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

# Entrada: Definida no código ou solicitada ao usuário
string = input("Informe uma string: ")
resultado = verificar_letra_a(string)
print(resultado)