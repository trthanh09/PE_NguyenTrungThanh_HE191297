import random
class Main:

    #====================GuessNumber function====================
    def GuessNumber(self, number):
        number = int(number)
        lowerlimit = 0
        higherlimit = number
        guess = random.randint(0, higherlimit)
        while True:
            respose = input(f"Is {guess} too high(h), too low(l), or correct(c): ")
            if respose.lower() == "h":
                higherlimit = guess
                guess = random.randint(lowerlimit + 1,higherlimit -1)
            elif respose.lower() == "l":
                lowerlimit = guess
                guess = random.randint(lowerlimit+ 1,higherlimit - 1)
            elif respose.lower() == "c":
                print(f"Welldone! The computer guessed your number {guess} correctly")
                break

#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("FINISH")
main = Main()
main.main()
