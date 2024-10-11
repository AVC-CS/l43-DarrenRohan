def main():
    total = 0
    i = 0

    while i < 5:
        numin = int(input("Enter number: "))
        total += numin
        i += 1
    print (total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
