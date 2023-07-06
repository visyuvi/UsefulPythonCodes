import queue
import random

# no of maximum elements in queue
N = 5

run = True
nums = queue.Queue()


def menu():
    global run
    print("MENU")
    print("1. Add random number to queue")
    print("2. Display queue entries. ")
    print("3. Exit")
    print()
    x = input("Enter choice")
    if x == "3":
        print("Exiting")
        run = False
    elif x == "1":
        if nums.qsize() == N:
            nums.get()
        r = random.randint(10, 50)
        nums.put(r)
        print("Added " + str(r) + " to Queue")
        print()

    elif x == "2":
        if nums.qsize() == 0:
            print("Empty")
            print()
        else:
            for i, item in enumerate(nums.queue):
                if i == N - 1:
                    print(item)
                else:
                    print(item, end=" ")
            print()
    else:
        print("Invalid choice")


while run:
    menu()
