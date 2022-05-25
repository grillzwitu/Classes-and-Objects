class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        '''Changes the student name'''

        self.name = new_name

    def change_age(self, new_age):
        '''Changes the student age'''

        self.age = new_age

    def add_track(self, new_track):
        '''Adds a track or tracks to the student tracks'''

        self.tracks.append(new_track)

    def get_score(self):
        '''Gets the student score'''

        print(self.score)
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Bob.name, Bob.age, Bob.tracks)
