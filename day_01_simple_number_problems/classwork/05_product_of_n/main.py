def main() -> None:
    n : int = int(input("Enter a number: "))
    factorial : int = 1
    
    for i in range(n, 1 - 1, -1):
            factorial *= i

    print(factorial)
    
if __name__ == '__main__':
    main()