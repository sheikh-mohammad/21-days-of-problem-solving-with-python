# Question 1: Print Numbers from 1 to N
# Input: 5
# Output: 1 2 3 4 5
# ✨ Teaches basic loop construction.

def main() -> None:
    # Get integer input from the user to define the upper limit
    num : int = int(input("Enter a number: "))
    
    # Iterate from 1 up to and including 'num'
    # range(start, stop) includes start but excludes stop, so we use num + 1
    for i in range(1, num + 1):
        # Print the current number with a space separator instead of a newline
        print(i, end=" ")

if __name__ == '__main__':
    main()