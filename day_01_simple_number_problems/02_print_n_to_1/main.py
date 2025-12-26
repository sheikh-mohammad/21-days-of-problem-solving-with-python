def main() -> None:
    # Get integer input from the user to define the upper limit
    end_num : int = int(input("Enter a number: "))
    
    # Iterate from 1 up to and including 'num'
    # range(start, stop) includes start but excludes stop, so we use num + 1
    for num in range(1, end_num + 1):
        # Print the current number with a space separator instead of a newline
        print(num, end=" ")

if __name__ == '__main__':
    main()