# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def exact_change(user_total):
  """Returns the number of each type of coin needed to make change for user_total.

  Args:
    user_total: The amount of change to make.

  Returns:
    A tuple of the number of dollars, quarters, dimes, nickels, and pennies needed.
  """

  num_dollars = user_total // 100
  user_total -= num_dollars * 100
  num_quarters = user_total // 25
  user_total -= num_quarters * 25
  num_dimes = user_total // 10
  user_total -= num_dimes * 10
  num_nickels = user_total // 5
  user_total -= num_nickels * 5
  num_pennies = user_total

  return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


def main():
  """Prompts the user for the amount of change and prints the change using the fewest coins."""

  input_val = int(input("Enter the amount of change: "))
  num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

  print("Here is your change in the fewest coins:")
  if num_dollars:
    print(f"{num_dollars} dollar")
  if num_quarters:
    print(f"{num_quarters} quarter")
  if num_dimes:
    print(f"{num_dimes} dime")
  if num_nickels:
    print(f"{num_nickels} nickel")
  if num_pennies:
    print(f"{num_pennies} pennies")


if __name__ == "__main__":
  main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
