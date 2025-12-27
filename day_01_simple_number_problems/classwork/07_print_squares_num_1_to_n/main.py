def main() -> None:
    n : int = int(input("Enter a number: "))
    
    for num in range(1, n + 1):
        print(num ** 2, end=" ")

if __name__ == '__main__':
    main()