# Functional Treat - Data Analyzer and Transformer

data_1d = []
data_2d = []
data_type = ""

total_values = 0
overall_mean = 0


# A - Built in functions
def display_summary():
    """Shows basic information about the data."""

    if data_type == "":
        print("Please enter data first.")
        return

    values = get_values()

    print("\nData Summary")
    print("Total elements:", len(values))
    print("Minimum:", min(values))
    print("Maximum:", max(values))
    print("Sum:", sum(values))
    print("Average:", round(sum(values) / len(values), 2))


# B - User defined functions
def calculate_average(values):
    """Calculates average of values."""

    return sum(values) / len(values)


def find_duplicates(values):
    """Finds duplicate values."""

    duplicates = []

    for x in values:
        if values.count(x) > 1 and x not in duplicates:
            duplicates.append(x)

    return duplicates


def get_unique_values(values):
    """Gets unique values."""

    unique = []

    for x in values:
        if x not in unique:
            unique.append(x)

    return unique


def display_2d_grid(grid):
    """Displays 2D list like a grid."""

    for row in grid:
        print(row)


# C - *args, **kwargs and __doc__
def show_values(*args):
    """Shows values using *args."""

    for x in args:
        print(x)


def show_info(**kwargs):
    """Shows information using **kwargs."""

    for key, value in kwargs.items():
        print(key, ":", value)


def show_docs():
    """Shows some function docstrings."""

    print(calculate_average.__doc__)
    print(find_duplicates.__doc__)
    print(get_unique_values.__doc__)


# D - Recursion
def factorial(n):
    """Finds factorial using recursion."""

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    """Finds Fibonacci number using recursion."""

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# E - Lambda functions
def filter_data(values, limit):
    """Filters values using lambda."""

    return list(filter(lambda x: x >= limit, values))


def scale_data(values, number):
    """Scales values using lambda."""

    return list(map(lambda x: x * number, values))


# F - global keyword
def update_summary(values):
    """Updates global variables."""

    global total_values
    global overall_mean

    total_values = len(values)
    overall_mean = calculate_average(values)


# G - Multiple return values
def get_statistics(values):
    """Returns four statistics."""

    minimum = min(values)
    maximum = max(values)
    total = sum(values)
    average = calculate_average(values)

    return minimum, maximum, total, average


# H - 1D and 2D data
def get_values():
    """Gets all data as a 1D list."""

    if data_type == "1D":
        return data_1d

    values = []

    for row in data_2d:
        for x in row:
            values.append(x)

    return values


def input_data():
    """Inputs 1D or 2D data."""

    global data_1d
    global data_2d
    global data_type

    print("\n1. Enter 1D data")
    print("2. Enter 2D data")
    print("3. Sample 1D data")
    print("4. Sample 2D data")

    choice = input("Choose: ")

    if choice == "1":

        data_1d = list(map(float, input("Enter numbers: ").split()))
        data_2d = []
        data_type = "1D"

        update_summary(data_1d)

        print("Data saved.")

    elif choice == "2":

        rows = int(input("Number of rows: "))

        data_2d = []

        for i in range(rows):
            row = list(map(float, input("Enter row: ").split()))
            data_2d.append(row)

        data_1d = []
        data_type = "2D"

        update_summary(get_values())

        print("Data saved.")
        display_2d_grid(data_2d)

    elif choice == "3":

        data_1d = [34, 12, 56, 78, 43, 21, 90]
        data_2d = []
        data_type = "1D"

        update_summary(data_1d)

        print(data_1d)

    elif choice == "4":

        data_2d = [
            [4, 8, 1],
            [9, 2, 6],
            [3, 7, 5]
        ]

        data_1d = []
        data_type = "2D"

        update_summary(get_values())

        display_2d_grid(data_2d)

    else:
        print("Wrong choice.")


# I - Sorting
def sort_data():
    """Sorts the data."""

    if data_type == "1D":

        a = data_1d.copy()

        print("1. Ascending")
        print("2. Descending")

        choice = input("Choose: ")

        if choice == "1":
            a.sort()
        elif choice == "2":
            a.sort(reverse=True)
        else:
            print("Wrong choice.")
            return

        print("Sorted data:", a)

    elif data_type == "2D":

        a = sorted(data_2d, key=lambda row: sum(row))

        print("Rows sorted by their sum:")
        display_2d_grid(a)

    else:
        print("Please enter data first.")


def recursion_menu():
    """Menu for factorial and Fibonacci."""

    print("\n1. Factorial")
    print("2. Fibonacci")

    choice = input("Choose: ")

    n = int(input("Enter number: "))

    if choice == "1":
        print("Answer:", factorial(n))

    elif choice == "2":
        print("Answer:", fibonacci(n))

    else:
        print("Wrong choice.")


def lambda_menu():
    """Menu for filter and scale."""

    values = get_values()

    if len(values) == 0:
        print("Please enter data first.")
        return

    print("\n1. Filter")
    print("2. Scale")

    choice = input("Choose: ")

    if choice == "1":

        limit = float(input("Enter limit: "))

        print(filter_data(values, limit))

    elif choice == "2":

        number = float(input("Enter scale number: "))

        print(scale_data(values, number))

    else:
        print("Wrong choice.")


def statistics():
    """Displays statistics using multiple return values."""

    values = get_values()

    if len(values) == 0:
        print("Please enter data first.")
        return

    minimum, maximum, total, average = get_statistics(values)

    print("\nDataset Statistics")
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Sum:", total)
    print("Average:", round(average, 2))


def main():
    """Runs the main program."""

    while True:

        print("\n==============================")
        print("Data Analyzer and Transformer")
        print("==============================")
        print("1. Input Data")
        print("2. Display Data Summary")
        print("3. Factorial / Fibonacci")
        print("4. Filter & Scale Data")
        print("5. Sort Data")
        print("6. Dataset Statistics")
        print("7. Exit")

        choice = input("Please enter your choice: ")

        if choice == "1":
            input_data()

        elif choice == "2":
            display_summary()

        elif choice == "3":
            recursion_menu()

        elif choice == "4":
            lambda_menu()

        elif choice == "5":
            sort_data()

        elif choice == "6":
            statistics()

        elif choice == "7":
            print("Thank you! for using program")
            break

        else:
            print("Invalid choice.")


main()
