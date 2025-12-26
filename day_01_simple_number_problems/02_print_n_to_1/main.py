def main() -> None:
    end_num : int = int(input("Enter a number: "))
    
    for num in range(end_num, 1 - 1, -1):
        print(num, end=" ")

if __name__ == '__main__':
    main()