import csv
import os
import shutil

class Staff:
    def __init__(self, file):
        self.file = file
        self.staff = {}
        self.fieldnames=['name','position','team','points']
        with open(self.file, newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.fieldnames)
            next(csvfile)
            for row in reader:
                self.staff[row["name"]] = [row["position"], row["team"], row["points"]]
        self.update_sheet()

    def add_points(self, name, points):
        self.staff[name][2]= str(int(self.staff[name][2]) + points)
        self.update_sheet()

    def subtract_points(self, name, points):
        self.staff[name][2]= str(int(self.staff[name][2]) - points)
        self.update_sheet()

    def add_staff(self, name, position, team, points):
        self.staff[name] = [position, team, points]
        self.update_sheet()

    def remove_staff(self, name):
        if name in self.staff:
            del self.staff[name]
            self.update_sheet()

    def update_sheet(self):
        #Updates the csv file and reorders it based on point values
        with open(self.file, "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
            for key, value in sorted(self.staff.items(), key=lambda e: int(e[1][2]), reverse=True):
                writer.writerow({'name': key, "position": self.staff[key][0], "team": self.staff[key][1], "points": self.staff[key][2]})

class Duties:
    def __init__(self, file):
        self.file = file
        self.tasks= {}
        self.fieldnames=['task','frequency','points']
        with open(self.file, newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.fieldnames)
            next(csvfile)
            for row in reader:
                self.tasks[row["task"]] = [row["frequency"], row["points"]]


    def point_value(self, task):
        return self.tasks[task][1]
'''
    def subtract_points(self, name, points):
        self.staff[name][2]= str(int(self.staff[name][2]) - points)
        self.update_sheet()

    def add_staff(self, name, position, team, points):
        self.staff[name] = [position, team, points]
        self.update_sheet()

    def remove_staff(self, name):
        if name in self.staff:
            del self.staff[name]
            self.update_sheet()

    def update_sheet(self):
        #Updates the csv file and reorders it based on point values
        with open(self.file, "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
            for key, value in sorted(self.staff.items(), key=lambda e: int(e[1][2]), reverse=True):
                writer.writerow({'name': key, "position": self.staff[key][0], "team": self.staff[key][1], "points": self.staff[key][2]})
'''


if __name__ == '__main__':
    m = Staff('staff.csv')
    n = Duties('maintenance.csv')
