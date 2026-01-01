def main() -> None:
    # Get integer input from the user for the starting number
    start_num : int = int(input("Enter a number: "))
    
    # Iterate from 'start_num' down to 1
    # range(start, stop, step)
    # start = start_num
    # stop = 0 (calculated as 1 - 1, so the loop includes 1 but excludes 0)
    # step = -1 (decrements the counter)
    for num in range(start_num, 1 - 1, -1):
        print(num, end=" ")

if __name__ == '__main__':
    main()