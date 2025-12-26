def main() -> None:
    n : int = int(input("Enter a number: "))
    sum : int = 0
    for num in range(1, n + 1):
        sum += num
        
    print(sum)

if __name__ == '__main__':
    main()