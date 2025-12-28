def main() -> None:
    n : int = int(input("Enter a number: "))
    
    sum_of_odd : int = 0
    
    odds : list[int | str] = []
    
    for num in range(1, n + 1):
        if num % 2 != 0:
            sum_of_odd += num
            odds.append(num)
            
    state = " + ".join([str(odd) for odd in odds])
    
    print(sum_of_odd, f"( {state} )")

if __name__ == '__main__':
    main()