def main() -> None:
    try:
        number_1 : int = int(input("Enter First number: "))
        number_2 : int = int(input("Enter Second Number: "))
        number_3 : int = int(input("Enter Third Number: "))
        if number_1 >= number_2 and number_1 >= number_3:
            print(number_1)
        elif number_2 >= number_1 and number_2 >= number_3:
            print(number_2)
        else:
            print(number_3)
    except ValueError:
        print("Invalid Input!")
    except Exception as e:
        print(f"Error occured: {e}")

if __name__ == '__main__':
    main()