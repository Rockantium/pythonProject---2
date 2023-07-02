# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def exact_change(user_total):
  """
  This function takes an integer as input and returns the number of dollars, quarters, dimes, nickels, and pennies needed to make up that amount in change.

  Args:
    user_total: The total change amount in cents.

  Returns:
    A tuple of (dollars, quarters, dimes, nickels, pennies).
  """

  dollars = user_total // 100
  user_total %= 100
  quarters = user_total // 25
  user_total %= 25
  dimes = user_total // 10
  user_total %= 10
  nickels = user_total // 5
  pennies = user_total % 5

  return (dollars, quarters, dimes, nickels, pennies)


if __name__ == '__main__':
  input_val = int(input())
  dollars, quarters, dimes, nickels, pennies = exact_change(input_val)

  if input_val <= 0:
    print('no change')
  else:
    if dollars > 1:
      print(f'{dollars} dollars')
    elif dollars == 1:
      print(f'{dollars} dollar')
    if quarters > 1:
      print(f'{quarters} quarters')
    elif quarters == 1:
      print(f'{quarters} quarter')
    if dimes > 1:
      print(f'{dimes} dimes')
    elif dimes == 1:
      print(f'{dimes} dime')
    if nickels > 1:
      print(f'{nickels} nickels')
    elif nickels == 1:
      print(f'{nickels} nickel')
    if pennies > 1:
      print(f'{pennies} pennies')
    elif pennies == 1:
      print(f'{pennies} penny')
