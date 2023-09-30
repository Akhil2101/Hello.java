fruits=["Apple","Orange","Banana","Peer"]
try:
    def make_pie(index):
        fruit = fruits[index]
        print(fruit + " pie")


    make_pie(4)
except IndexError:
    print("fruit pie")


