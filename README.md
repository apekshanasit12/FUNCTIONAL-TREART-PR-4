# FUNCTIONAL-TREART-PR-4
# Functional Treat – Data Analyzer and Transformer

A menu-driven Python program that analyzes and transforms data stored in
**1D and 2D lists (arrays)**. It is built entirely from functions and is
written in a simple, beginner-friendly style.

## Project Objective

Let users analyze and transform data in different ways by choosing options
from a console menu, while demonstrating these Python topics:

- Built-in functions
- User-defined functions (UDF)
- `*args`, `**kwargs`, and `__doc__`
- Function recursion
- Lambda (anonymous) functions
- The `global` keyword
- Returning multiple values
- Sorting and transforming list-based data

## Requirements

- Python 3.6 or newer
- No external libraries needed (uses only built-in Python)

## How to Run

```bash
python functional_treat_beginner.py
```

## Main Menu

```
Welcome to the Data Analyzer and Transformer Program

Main Menu:
1. Input Data (1D or 2D)
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial / Fibonacci (Recursion)
4. Filter & Scale Data (Lambda Functions)
5. Sort Data
6. Display Dataset Statistics (Multiple Return Values)
7. Exit Program
Please enter your choice:
```

Enter a number from 1 to 7. Any other input shows an error message and the
menu appears again. Option 7 exits the program.

> **Tip:** Use option 1 first. Options 2, 4, 5 and 6 need data to work with.

## Menu Options Explained

| Option | What it does | Topic demonstrated |
|--------|--------------|--------------------|
| 1 | Enter a 1D or 2D list manually, or load sample data | 1D / 2D arrays, global variables |
| 2 | Shows total elements, minimum, maximum, sum and average | Built-in functions (`len`, `min`, `max`, `sum`) |
| 3 | Calculates the factorial or a Fibonacci number | Recursion |
| 4 | Keeps values at or above a threshold, then scales all values | Lambda with `filter()` and `map()` |
| 5 | Sorts the 1D list (ascending/descending) or the rows of the 2D list | `sort()` vs `sorted()` |
| 6 | Shows minimum, maximum, sum and average | Returning multiple values |
| 7 | Exits the program | Menu control |

### Option 1 – Input Data

Choose one of four sub-options:

1. Enter a 1D list manually (numbers separated by spaces)
2. Enter a 2D list manually (you give the number of rows, then each row)
3. Use sample 1D data: `[34, 12, 56, 78, 43, 21, 90]`
4. Use sample 2D data: `[[4, 8, 1], [9, 2, 6], [3, 7, 5]]` (shown as a grid)

### Option 5 – Sort Data

- **1D data:** uses `list.sort()` on a copy of the list, in ascending or
  descending order.
- **2D data:** uses `sorted()` to order the rows by their sum. It returns a
  **new** list, so the original grid is not changed. This shows the
  difference between in-place sorting (`sort()`) and returning a new sorted
  list (`sorted()`).

## Example Console Interaction

Using sample data `34 12 56 78 43 21 90`:

```
Please enter your choice: 2

Data Summary:
- Total elements: 7
- Minimum value: 12
- Maximum value: 90
- Sum of all values: 334
- Average value: 47.71

Please enter your choice: 3

1. Calculate Factorial
2. Calculate Fibonacci number
Choose an option: 1
Enter a whole number: 5
Factorial of 5 is: 120

Please enter your choice: 6

Dataset Statistics:
- Minimum value: 12
- Maximum value: 90
- Sum of all values: 334
- Average value: 47.71
```

## How the Requirements Are Covered

| Section | Requirement | Where in the code |
|---------|-------------|-------------------|
| A | Built-in functions | `display_data_summary()` |
| B | User-defined functions | `calculate_average()`, `find_duplicates()`, `get_unique_values()`, `display_2d_grid()` |
| C | `*args`, `**kwargs`, `__doc__` | `show_values(*args)`, `print_dataset_characteristics(**kwargs)`, and a docstring in every function (`show_all_docstrings()` prints them) |
| D | Recursion | `factorial()` and `fibonacci()` |
| E | Lambda with `map()` / `filter()` | `filter_by_threshold()` and `scale_data()` |
| F | `global` keyword | `update_global_summary()` updates the global `total_values` and `overall_mean` |
| G | Return multiple values | `get_statistics()` returns minimum, maximum, sum and average |
| H | 1D and 2D lists, grid display | `input_data()` and `display_2d_grid()` |
| I | Sorting | `sort_1d_data()` (`sort()`) and `sort_2d_rows()` (`sorted()`) |

## Code Structure

The program file is organized into labelled sections that match the
requirement letters above:

1. Global variables (`data_1d`, `data_2d`, `total_values`, `overall_mean`)
2. Sections A–I: the functions listed in the table above
3. Menu handler functions (one per menu option)
4. `print_menu()` and `main()`, which run the menu loop until the user exits

## Documentation

Every function has a `__doc__` docstring describing its purpose. You can
read one in a Python shell, for example:

```python
print(calculate_average.__doc__)
```

## Notes

- Values can be whole numbers or decimals (for example `3 5.5 7`).
- Data entered in option 1 stays stored until you replace it or exit.
- Sorting never modifies your stored data; it works on a copy or returns a
  new list.
