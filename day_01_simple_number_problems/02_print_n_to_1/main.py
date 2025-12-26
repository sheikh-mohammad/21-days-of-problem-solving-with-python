def main() -> None:
    """Reads a number from user input and prints numbers from N to 1.

    This function prompts the user for an integer input N, then iterates 
    downwards from N to 1 (inclusive), printing each number separated by a space.
    """
    # Get integer input from the user for the starting number
    end_num : int = int(input("Enter a number: "))
    
    # Iterate from 'end_num' down to 1
    # range(start, stop, step)
    # start = end_num
    # stop = 0 (calculated as 1 - 1, so the loop includes 1 but excludes 0)
    # step = -1 (decrements the counter)
    for num in range(end_num, 1 - 1, -1):
        print(num, end=" ")

if __name__ == '__main__':
    main()