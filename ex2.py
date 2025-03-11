def somatorio(n: int) -> int:
    if (n == 0):
        return 0
    
    if (n > 0):
        return n + somatorio(n -1)
    else:
        return n + somatorio(n +1)


def main():
    print("Multiplicação por somas sucessivas")
    print("----------------------------------")
    
    try:
        # Solicita o número ao usuário
        n = int(input("Digite um número: "))

        # Calcula e exibe o resultado
        resultado = somatorio(n)
        print(resultado)
            
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")


if __name__ == "__main__":
    main()