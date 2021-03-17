def main():
    string = input("Player 1, enter your choice (R/P/S): ")
    choice1 = str(string)
    string = input("Player 2, enter your choice (R/P/S): ")
    choice2 = str(string)
    if choice1 == "P" and choice2 == "R":
        print("Player 1 won!")
    elif choice1 == "R" and choice2 == "S":
        print("Player 1 won!")
    elif choice1 == "S" and choice2 == "P":
        print("Player 1 won!")
    elif choice1 == choice2:
        print("It's a tie!")
    else:
        print("Player 2 won!")


if __name__ == "__main__":
    main()





