class workout:
    def __init__(self, name, sets, date):
        self.name = name
        self.sets = sets
        self.date = date
    def displayWorkout(self):
        print(f"--------------------------------------\nWorkout: {self.name} \nSets performed: {self.sets} \nDate: {self.date}\n--------------------------------------\n")
        





