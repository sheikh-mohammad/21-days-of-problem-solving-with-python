def main() -> None:
    n : int = int(input("Enter a number: "))
    factorial : int = 1
    
    for num in range(n, 1 - 1, -1):
            factorial *= num

    print(factorial)
    
if __name__ == '__main__':
    main()