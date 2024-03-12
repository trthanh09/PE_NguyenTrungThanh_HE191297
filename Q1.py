import math
class Main:
    
    #====================f1====================
    def f1(self, inputString):
        move = inputString.split(',')
        for i in move:
            print(i)
    #====================f2====================
    def f2(self, inputString):
        x = 0
        y = 0
        for movement in inputString:
            diraction, steps = movement.split()
            steps = int(steps)
            if direction == 'UP':
                y += steps
            elif direction == 'DOWN':
                y -= steps
            elif direction == 'LEFT':
                x -= steps
            elif direction == 'RIGHT':
                x += steps
        distance = math.sqrt(x**2 + y**2)
        return round(distance)
  
        movements = inputString
        distance = calculate(inputString.split(', '))
        print(distance)
#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (2 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        inputString = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(inputString)
        elif choice == 2:
            self.f2(inputString)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()
