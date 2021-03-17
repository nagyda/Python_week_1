def main():
    string = input("Purchase price: ")
    price = int(string)
    string = input("Paid amount of money: ")
    amount = int(string)

    string = (amount - price)
    full_change = int(string)

    string = (full_change // 10)
    first = int(string)

    string = (full_change % 10 // 5)
    second = int(string)

    string = (full_change % 10 % 5 // 2)
    third = int(string)

    string = (full_change % 10 % 5 % 2 // 1)
    fourth = int(string)

    if amount > price:
        print("Offer change: ")

    if full_change == 0:
        print("No change")

    if amount < price:
        print("No change")

    if first > 0:
        print(full_change // 10, "ten-euro notes")
    else:
        pass

    if second > 0:
        print(full_change % 10 // 5, "five-euro notes")
    else:
        pass

    if third > 0:
        print(full_change % 10 % 5 // 2, "two-euro coins")
    else:
        pass

    if fourth > 0:
        print(full_change % 10 % 5 % 2 // 1, "one-euro coins")
    else:
        pass


if __name__ == "__main__":
    main()
