def main():
    string = input("How do you feel? (1-10) ")
    mood = int(string)
    if 1 <= mood <= 10:
        if 4 <= mood <= 7:
            print("A suitable smiley would be :-|")
        elif 10 > mood > 7:
            print("A suitable smiley would be :-)")
        elif 1 < mood < 4:
            print("A suitable smiley would be :-(")
        elif mood == 1:
            print("A suitable smiley would be :'(")
        elif mood == 10:
            print("A suitable smiley would be :-D")
    else:
        print("Bad input!")


if __name__ == "__main__":
    main()
