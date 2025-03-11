def offset(k: int, j: int) -> int:
    if k == j:
        return k
    
    if k > j:
        return offset(j, k)
    else:
        return k + offset(k + 1, j)
    

def main():
    print("Soma do intervalo")
    print("----------------------------------")
    
    try:
        # Solicita o número ao usuário
        k = int(input("Digite um número (k): "))
        j = int(input("Digite um número (j): "))

        # Calcula e exibe o resultado
        resultado = offset(k, j)
        print(resultado)

            
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")


if __name__ == "__main__":
    main()