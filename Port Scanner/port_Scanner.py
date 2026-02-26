import random
import subprocess


def pinging():
    for a in range(0, 256):
        base = "192.168.43."
        ip = base + str(a)
        result = subprocess.run(["ping ", "-c", "1", ip], capture_output=True)
        print(ip)

        if (result.returncode != 0):
            continue

        print(result.returncode())

# pinging()


def iprinter():
    base = "192.168.43."
    for a in range(0, 256):
        ip = base + str(a)
        subprocess.run(["nmap ", "-sS", ip], text=True)

# iprinter()


# we use the 0 as true because in binary and C code 0 means no errors and fully correct code so 0 means true and any other number means that much number of errors
# so this is why we use 0 as trua and other numbers as false
# capture output catches the output and just give a specific thing such as error code like 0 means no error and 1 or any other number means some error.

# thats it for today means 17/02/2026
# its 12:12 and now i will shut down the PC and go to sleep


def understanding_subprocess():
    x = subprocess.run(["ping", "192.168.43.173"], capture_output=True)
    print(x.returncode)
    return x.returncode

# if understanding_subprocess() == 0:
#     print("good")
# else:
#     print("bad")


# getting functions

# name = input("Enter your name : ")

# def abc(name) :
#     print("hello " + name)

# abc("Aaryan")


# hangman game


def game():
    wordlist = ["hacker", "laptop", "personal computer"]
    guess = input("Enter the a random letter : ").lower()
    secret = random.choice(wordlist)
    for i in secret:
        if i == guess:
            print("good guess")
            break
        else:
            print("no letter")


game()
