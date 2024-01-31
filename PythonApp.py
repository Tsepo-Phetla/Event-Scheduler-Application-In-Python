class Event:
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time


class EventManager:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def view_events(self):
        for i, event in enumerate(self.events):
            print(f"{i + 1}. Title: {event.title}, Date: {event.date}, Time: {event.time}")

    def delete_event(self, index):
        if 0 <= index < len(self.events):
            del self.events[index]
            print("Event deleted successfully.")
        else:
            print("Invalid index. Please enter a valid index.")


def main():
    event_manager = EventManager()

    while True:
        print("\nMenu:")
        print("1. Add Event")
        print("2. View Events")
        print("3. Delete Event")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            date = input("Enter event date: ")
            time = input("Enter event time: ")

            new_event = Event(title, description, date, time)
            event_manager.add_event(new_event)
            print("Event added successfully.")

        elif choice == "2":
            event_manager.view_events()

        elif choice == "3":
            index = int(input("Enter the index of the event to delete: ")) - 1
            event_manager.delete_event(index)

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
