# Question 1: Print Numbers from 1 to N
# Input: 5
# Output: 1 2 3 4 5
# ✨ Teaches basic loop construction.

def main() -> None:
    num : int = int(input("Enter a number: "))
    
    for i in range(1, num + 1):
        print(i, end=" ")

if __name__ == '__main__':
    main()