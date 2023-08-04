
############ Q5

class myStringClass:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

def test():
    # Create an instance of the class
    manipulator = myStringClass()

    # Call the getString method to get a string from the user
    manipulator.getString()

    # Call the printString method to print the string in upper case
    manipulator.printString()

# Call the test function to test the class methods
test()

