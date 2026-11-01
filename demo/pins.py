'''
Authors     : Aaron Sapp & Warren Nixon
Date        : Oct. 31, 2026
Course      : CSCI-2996-A01-SPECIAL TOPICS: Problem Solving
Module      : pins.py
Description : User can create, delete, and view pins
'''

# User class
class User:
    def __init__(self):
        # Pins list
        self.pins = []

    # Main
    # Where most of the code goes
    def main(self):
        print("----- Pins -----")
        print(" - Create a Pin")
        print(" - Delete a Pin")
        print(" - Show Report")
        print(" - Quit")
        print("----------------")

        user_input = input("Please enter one of the following: ").lower()

        # Iterates indefinitely until the user quits
        while True:

            # Sets to false after each iteration
            # Sets to true if the user enters an invalid response
            invalid_response = False

            # Checks if any pins exist
            any_pins = len(self.pins) > 0

            match user_input:

                # Creates pins
                case "create":
                    self.create_pin()

                # Deletes pins
                case "delete":

                    # Only deletes pins if there is at least one pin
                    if any_pins:
                        self.delete_pins()

                    else:
                        print("There are no current pins to delete.")
                        
                # Shows current pins
                case "show":
                    
                    # Iterates through pins and prints its info
                    # Only iterates if there is at least one pin
                    if any_pins:
                        self.show_pins()

                    else:
                        print("There are no current pins to show.")

                # Quits the program
                case "quit":
                    break

                # Invalid response
                case _:
                    invalid_response = True
                    user_input = input("Please enter a proper command: ").lower()

            # Asks the user again
            # Will not ask the user again if they entered an invalid response before
            if not invalid_response:
                print("----- Pins -----")
                print(" - Create a Pin")
                print(" - Delete a Pin")
                print(" - Show Report")
                print(" - Quit")
                print("----------------")

                user_input = input("Please enter one of the following: ").lower()

    # Create pins
    def create_pin(self):
        print("----- Types -----")
        print(" - Clear")
        print(" - Caution")
        print(" - Warning")
        print("-----------------")

        user_input = input("Please enter the type for your pin: ").lower()

        # Get pin type
        while True:
            match user_input:

                # Pin Types
                # Set pin type to user response if user enters the following
                case "clear" | "caution" | "warning":
                    pin_type = user_input.capitalize()
                    break

                # Quits out of current action
                case "quit":
                    print('Current pin has been discarded.')
                    return

                # Checks for invalid responses
                # Prompts the user to enter a proper pin type
                case _:
                    user_input = input("Invalid response. Please enter a proper type: ").lower()

        # Create and add pin to current pins
        pin = self.Pin((pin_type))
        self.pins.append(pin)
        print(f"Pin {self.pins.index(pin) + 1} has been created.")

    # Delete pins
    def delete_pins(self):
        user_input = input("Which pin would you like to delete (must be the number assigned to the pin) (type 'show' to show each pin's number and their info): ").lower()

        while True:

            # Sets to false after each iteration
            # Sets to true if the user enters an invalid response
            invalid_response = False

            try:
                # Convert user input to integer
                user_number = int(user_input)

                # Deletes selected pin
                try:
                    print(f"Pin {user_number} has been deleted.")
                    self.pins.pop(user_number - 1)
                    break

                # Catches out of scope responses
                except:
                    user_input = input("Invalid response. Please enter a pin available (must be the number assigned to the pin) (type 'show' to show each pin's number and their info): ").lower()
                    invalid_response = True

            # Catches non-integer responses
            except ValueError:
                match user_input:

                    # Show current pins
                    case "show":
                        self.show_pins()

                    # Quits the current action
                    case "quit":
                        print("Deletion has been canceled.")
                        return

                    # Prompts the user to enter an integer (or a proper command)
                    case _:
                        user_input = input("Invalid response. Please enter the pin you would like to delete (must be the number assigned to the pin) (type 'show' to show each pin's number and their info): ").lower()
                        invalid_response = True

            # Asks the user again
            # Will not ask the user if they entered an invalid response before
            if not invalid_response:
                user_input = input("Which pin would you like to delete (must be the number assigned to the pin) (type 'show' to show each pin's number and their info): ").lower()

    # Shows pins
    def show_pins(self):
        for index, pin in enumerate(self.pins, start = 1):
            print(f"Pin {index} | Type: {pin.pin_type}")

    # Pin Class
    class Pin:
        def __init__(self, pin_type):
            self.pin_type = pin_type

# Test
user = User()
user.main()
