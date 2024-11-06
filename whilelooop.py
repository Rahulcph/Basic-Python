while True:
    x = input("Enter a number: ")# input is always a text/string
    x = int(x)

    if x == 'q':
        break

    elif x%2 == 0:
        print("Even")
    else:


        print("Odd")
                    