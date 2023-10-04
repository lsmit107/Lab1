# Number Analyzer
if __name__ == "__main__":
    name = (input("What is your name?"))

keep_running = True
while keep_running == True:
    num = int(input("Hello," + name + " , Enter a number between 1 and 100"))
    if num < 60 and num % 2 != 0:
        print(num)
        print("The number entered is odd and less than 60.")
    elif num in range(1, 25) and num % 2 == 0:
        print(num)
        print("Even and less than 25.")
    elif num in range(25, 61) and num % 2 == 0:
        print(num)
        print("Even and less than 25.")
    elif num in range(60, 101) and num % 2 == 0:
        print(num)
        print("Even and greater than 60.")
    elif num in range(60, 101) and num % 2 != 0:
        print(num)
        print("Even and less than 25.")
    continue_choice = input("Do you want to continue? yes/no")
    if continue_choice == "yes":
        keep_running = True
    elif continue_choice == "no":
        keep_running = False





