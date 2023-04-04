#if statements problem-----------------------------------------------
bench = int(input("How much can you bench?: "))

if bench <10:
    print("Keep practicing and you'll eventually get better")
elif bench > 10 and bench < 50:
    print("You're getting good at this")
elif bench > 50:
    print("You're swol")


#for loop problem-----------------------------------------------
for i in range(20, 52, 2):
    print(i, end = " ")

#while loop problem-----------------------------------------------
word = "ribbit"

while word != "frog":
    print("Ribbit")
    word = input("type anything you want but type frog to quit: ")

print("You typed frog")

#while loop problem-----------------------------------------------
num = 100
while num >= 50:
    print(num, end = " ")
    num-=5

#function problem-----------------------------------------------
def AvgTwoNums(x, y):
   
    add = (x + y) / 2

    return add

print("The average number is", AvgTwoNums(8,4))




marbles = [4, 6, 2, 9]

print("The second element is", marbles[1])
for i in range(len(marbles)):
    marbles[i] *= 5
    print(marbles)

#class problem-----------------------------------------------
class fruit():
    def __init__(self, type, weight):
        self.type = type
        self.weight = weight
        self.isFresh = True

    def printInfo(self):
        print("The fruit type is ", self.type, ", the weight is", self.weight, "and their freshness status is", self.isFresh)

    def turnRotten(self):
        self.isFresh = False



fruit1 = fruit("Watermelon",10.0)
fruit2 = fruit("Strawberry",1.0)

while True:
    choice = int(input("press 1 to turn the Watermelon rotten, and 2 to turn the Strawberry rotten or 3 to check their info: "))

    if choice == 1:
        fruit1.turnRotten()
        print("The watermelon is rotten")
    elif choice == 2:
        fruit2.turnRotten()
        print("The strawberry is rotten")
    elif choice == 3:
        fruit1.printInfo()
        fruit2.printInfo()



