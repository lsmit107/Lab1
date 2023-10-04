if __name__ == "__main__":
    keep_running = True
    while keep_running:
        number = int(input("Choose a number"))
        print(f'{"Number":>6}\t{"Square" :>8}\t{"Cube" :>6}')

        for num in range(1, number + 1):
            square = num ** 2
            cube = num ** 3
            print(f'{num:>6}\t{square :>8}\t{cube :>6}')
        response = input(f"Continue? (y/n)")
        if response == "y":
            keep_running = True
        elif response == "n":
            keep_running = False
