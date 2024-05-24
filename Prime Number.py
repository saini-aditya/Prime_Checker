def prime_checker():
    num = int(input("Enter a number: "))

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


while True:
    yes_or_no = input("Press ENTER to number or enter '1' to EXIT: ")
    if yes_or_no == '1':
        break
    prime_checker()
