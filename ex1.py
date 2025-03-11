def fatorial(n: int) -> int:
    if (n == 1):
        return 1
    
    return n * fatorial(n -1)
    

def main():
    print("Multiplicação por somas sucessivas")
    print("----------------------------------")
    
    try:
        # Solicita o número ao usuário
        n = int(input("Digite um número: "))

        # Calcula e exibe o resultado
        resultado = fatorial(n)
        print(resultado)
            
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")


if __name__ == "__main__":
    main()