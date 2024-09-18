# Hub to execute the assignment

import vehicle
import event

# Execute Task 1
def run_vehicle_task():
    print("Vehicle Registration System")
    # Create instances of Vehicle
    car = vehicle.Vehicle("123ABC", "Car", "Alice")
    bike = vehicle.Vehicle("456XYZ", "Motorbike", "Bob")

    # Display vehicles
    print(car)
    print(bike)

    # Update the owner of the car
    car.update_owner("Charlie")
    print("\nAfter updating the car owner:")
    print(car)

# Execute Task 2
def run_event_task():
    print("\nEvent Management System Enhancement")
    # Create an instance of Event
    concert = event.Event("City Concert", "2024-10-15")

    # Add participants to the event
    concert.add_participant()
    concert.add_participant()
    concert.add_participant()

    # Display event details
    print(concert)

    # Get the current participant count
    print(f"Total participants: {concert.get_participant_count()}")


if __name__ == "__main__":
    # Run both tasks
    run_vehicle_task()
    run_event_task()
