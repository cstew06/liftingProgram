from workout import *

def main():
    my_sets = [Set("Bench Press", 185, 7), Set("Bench Press",185,9)]
    myWRKT = Workout("Chest and Back", my_sets, "today")
    myWRKT.displayDetails()
    myWRKT.displayWorkout()


if __name__ == '__main__':
    main()