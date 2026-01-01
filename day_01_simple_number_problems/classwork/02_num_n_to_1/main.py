def main() -> None:
    # Get integer input from the user for the starting number
    n : int = int(input("Enter a number: "))
    
    # Iterate from 'n' down to 1
    # range(start, stop, step)
    # start = n
    # stop = 0 (calculated as 1 - 1, so the loop includes 1 but excludes 0)
    # step = -1 (decrements the counter)
    for num in range(n, 1 - 1, -1):
        print(num, end=" ")

if __name__ == '__main__':
    main()