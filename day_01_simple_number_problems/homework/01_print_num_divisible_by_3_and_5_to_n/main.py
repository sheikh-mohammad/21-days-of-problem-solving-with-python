def main() -> None:
    n : int = int(input("Enter a number: "))
    
    for num in range(1, n + 1):
        if (num % 3 == 0) and (num % 5 == 0):
            print(num, end=" ")

if __name__ == '__main__':
    main()