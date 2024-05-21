def greeting(Mark):
    print("Hello, " + Mark + "!")

greeting("Mark")

def pack(a, b, c):
    return [a, b, c]

print(pack("a", "b", "c"))

def eat_lunch(my_list):
    if my_list == []:
        print("My lunchbox is empty!")
    else:
        print("First I eat " + my_list[0])
        my_list.pop(0)
        print("Next, I eat " + my_list[0])
        my_list.pop(0)
        print("And finally I eat " + my_list[0])
        my_list.pop(0)

eat_lunch(["sandwich", "apple", "banana", "orange", "kale", "broccoli", "carrot", "potato", "onion", "celery"])