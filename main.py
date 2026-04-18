class Member:
    def __init__(self, name, age, plan):
        self.name = name
        self.age = age
        self.plan = plan
        self.attendance = []

    def attend(self, date):
        self.attendance.append(date)

class Trainer:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.trainees = []

    def add_trainee(self, member):
        self.trainees.append(member)

class Plan:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Attendance:
    def __init__(self, date, member):
        self.date = date
        self.member = member

class Gym:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.trainers = []
        self.plans = []

    def add_member(self, member):
        self.members.append(member)

    def add_trainer(self, trainer):
        self.trainers.append(trainer)

    def add_plan(self, plan):
        self.plans.append(plan)

    def display_members(self):
        for member in self.members:
            print(f"Name: {member.name}, Age: {member.age}, Plan: {member.plan.name}")

    def display_trainers(self):
        for trainer in self.trainers:
            print(f"Name: {trainer.name}, Specialty: {trainer.specialty}")

    def display_plans(self):
        for plan in self.plans:
            print(f"Name: {plan.name}, Price: {plan.price}")

gym = Gym("Fitness Center")
plan1 = Plan("Basic", 50)
plan2 = Plan("Premium", 100)

member1 = Member("John Doe", 25, plan1)
member2 = Member("Jane Doe", 30, plan2)

trainer1 = Trainer("Trainer 1", "Yoga")
trainer2 = Trainer("Trainer 2", "Cardio")

gym.add_member(member1)
gym.add_member(member2)
gym.add_trainer(trainer1)
gym.add_trainer(trainer2)
gym.add_plan(plan1)
gym.add_plan(plan2)

gym.display_members()
gym.display_trainers()
gym.display_plans()

member1.attend("2024-01-01")
member2.attend("2024-01-02")

for member in gym.members:
    print(f"Member: {member.name}, Attendance: {member.attendance}")

trainer1.add_trainee(member1)
trainer2.add_trainee(member2)

for trainer in gym.trainers:
    print(f"Trainer: {trainer.name}, Trainees: {[trainee.name for trainee in trainer.trainees]}")