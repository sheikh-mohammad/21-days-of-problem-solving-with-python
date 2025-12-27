def main() -> None:
    n : int = int(input("Enter a number: "))
    sum_of_even : int = 0
    evens : list[str | int] = []
    
    for num in range(2, n + 1):
        if num % 2 == 0:
            sum_of_even += num
            evens.append(num)
            
    state : str = "+".join([str(even) for even in evens])            
            
    print(sum_of_even, f"( {state} )")

if __name__ == '__main__':
    main()