class Workout:
    def __init__(self, name, sets, date):
        self.name = name
        self.sets = sets
        self.date = date
    def displayDetails(self):
        print(f"--------------------------------------\nWorkout: {self.name} \nSets performed: {len(self.sets)} \nDate: {self.date}\n--------------------------------------\n")
    def displayWorkout(self):
        for set in self.sets:
            set.displaySet()

class Set:
    def __init__(self, exersize, weight, reps):
        self.exersize = exersize
        self.weight = weight
        self.reps = reps
    def displaySet(self):
        print(f"You performed {self.reps} reps of {self.weight} of {self.exersize}")






