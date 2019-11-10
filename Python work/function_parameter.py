def poweroftwo(num):
    num = int(num)
    result = 2 ** num
    result = int(result)
    print("The result is", result)
    return result


def main():
    num1 = input("Give a number:")
    poweroftwo(num1)


if __name__ == '__main__':
    main()