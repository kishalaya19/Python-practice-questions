def reverse_list(list):
    rev = list[::-1]
    return rev

list = input("give me a list: ")

rv = reverse_list(list)
print(f"the reveresed list is {rv}")