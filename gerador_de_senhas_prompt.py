import random
import string

def geradordesenhas(tamanho):
    # Definindo os caracteres que podem ser usados na senha
    letras = string.ascii_letters + string.digits + string.punctuation
    # Gerando uma senha aleatória
    senha = ''.join(random.choice(letras) for i in range(tamanho))
    return senha

# Exemplo de uso
tamanho = int(input("Insira o tamanho da senha: "))  # Comprimento desejado para a senha
senha = geradordesenhas(tamanho)
print(f"Senha gerada: {senha}")
