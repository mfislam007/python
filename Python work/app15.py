mynumber = input("Give a number:")
try:
    mynumber = int(mynumber)
    print("The output was suitable!")
except Exception:
    print("The output was malformed!")