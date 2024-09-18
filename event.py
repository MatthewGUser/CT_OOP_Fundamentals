# [ Task 2 ]

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count

    def __str__(self):
        """Return a string representation of the event details."""
        return f"Event({self.name} on {self.date}, Participants: {self.participant_count})"