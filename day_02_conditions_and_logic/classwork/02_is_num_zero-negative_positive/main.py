def main() -> None:
    
    try:
        number : int = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
    else:
        if number < 0:
            print("Negative")
        elif number > 0:
            print("Positive")
        else:
            print("Zero")

if __name__ == '__main__':
    main()