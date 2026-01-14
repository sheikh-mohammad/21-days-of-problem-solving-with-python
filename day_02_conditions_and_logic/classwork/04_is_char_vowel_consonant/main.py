def main() -> None:
  letter : str = input("Enter a letter: ")

  if len(letter) > 1:
    print("Please enter a single letter!")
  else:
    if letter.isalpha() == True:
      if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        print("Vowel")
      else:
        print("Constant")
    else:
      print("Please enter a alphabet letter")

if __name__ == '__main__':
  main()