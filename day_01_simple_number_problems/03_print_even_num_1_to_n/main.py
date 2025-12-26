def main() -> None:
    end_num : int = int(input("Enter a ending number: "))
    
    for num in range(1, end_num + 1):
        if num % 2 == 0:
            print(num, end=" ")

if __name__ == '__main__':
    main()