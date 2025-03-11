# Função recursiva
def verificar(s, inicio, fim):
    # Caso base: se o início for maior ou igual ao fim, é um palíndromo
    if inicio >= fim:
        return True
        
    # Verifica se os caracteres são iguais
    if s[inicio] != s[fim]:
        return False
        
    # Chamada recursiva
    return verificar(s, inicio + 1, fim - 1)

def palindromo(s):
    # Remove espaços e converte para minúsculas
    s = ''.join(s.split()).lower()
    return verificar(s, 0, len(s) - 1)


def main():
    print("Palindromo")
    print("----------------------------------")
    
    try:
        # Solicita o número ao usuário
        string = str(input("Digite o texto: "))
    
        # Calcula e exibe o resultado
        resultado = palindromo(string)
        print(resultado)

        
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas palavras.")


if __name__ == "__main__":
    main()