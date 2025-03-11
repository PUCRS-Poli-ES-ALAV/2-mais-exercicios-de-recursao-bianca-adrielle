def fibonacci(n: int) -> int:
    if n < 2:
        return n
    
    return fibonacci(n -1) + fibonacci(n -2)
    

def main():
    print("Fibonacci index")
    print("----------------------------------")
    
    try:
        # Solicita o número ao usuário
        n = int(input("Digite um número: "))

        if n < 0:
            print("Por favor, digite apenas números naturais (maiores ou iguais a zero).")
            return

        # Calcula e exibe o resultado
        resultado = fibonacci(n)
        print(resultado)

            
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")


if __name__ == "__main__":
    main()