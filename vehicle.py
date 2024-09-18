# [ Task 1 ]
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def __str__(self):
        return f"Vehicle({self.registration_number}, {self.type}, owned by {self.owner})"