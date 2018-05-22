import random
import time

n = 0
random_number = random.randint(1,101)

print ("Random Number {}".format(random_number))

def Dr_Strange_Bargain(n):
    print("Dr. Strange: Dormamu! I've come to bargain.\n")
    time.sleep(2)
    print("Dormamu: You've come to die.\n")
    print("Dormamu: Your world is now my world, like all worlds.\n")
    time.sleep(2)
    if n == 0:
        n = n+1
        Dr_Strange_Bargain(n)
    elif n == 1:
        time.sleep(2)
        print("Dormamu: What is this?\n")
        print("Dormamu: Illusion? - No, this is real.\n")
        time.sleep(2)
        n = n+1
        Dr_Strange_Bargain(n)
    elif (n > 1) & (n != random_number):
        time.sleep(2)
        print("Dormamu: You cannot do this forever.\n")
        print("Dormamu: No! Make it stop.\n")
        print("Dr. Strange: Actually, I can.\n This is how things are now.\n You and me, trapped in this moment, endlessly.")
        time.sleep(2)
        n = n+1
        Dr_Strange_Bargain(n)
    elif n == random_number:
        print("Dr.Strange: Take your zealots from this earth.\n End your assault on my world.\n Never come back")

Dr_Strange_Bargain(n)
