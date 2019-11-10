lists=[]
def addition(name):
    lists.append(name)
    return lists

def remove(number):
    del lists[number]
    return lists
count = 0
while True:
    select = int(input("""Would you like to
     (1)Add or
     (2)Remove items or
     (3)Quit?:"""))
    if select == 1:
            add = input("What will be added?: ")
            addition(add)
            count = count + 1
            count = int(count)
    elif select == 2:
            print("There are {} items in the list.".format(count))
            rem = int(input("Which item is deleted?:"))
            if rem < len(lists):
                remove(rem)
                count = count - 1
            else:
                print("Incorrect selection.")
    elif select == 3:
            print("The following items remain in the list:")
            for i in lists:
             print(i)
            break
    else:
        print("Incorrect selection.")