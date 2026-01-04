def main() -> None:
<<<<<<< HEAD
    pass
=======
    try:
        units : int = int(input("Enter units: "))
        total_bill : int = 0
    except ValueError:
        print("Invalid input!")
    except Exception as e:
        print(f"Error occurred: {e}")
    else:
        if units >= 0 and units <= 100:
            total_bill = units * 5
        elif units >= 101 and units <= 200:
            total_bill = units * 7
        elif units >= 201 and units <= 300:
            total_bill = units * 10
        elif units > 300:
            total_bill = units * 12
        else:
            total_bill = 0

        print(f"Total Bill = Rs {total_bill}")
    
>>>>>>> a50f5ca09287f193e715515a6613d3dde36cefcb

if __name__ == '__main__':
    main()