from helpers import *



def get_result():
  time = get_departure_time()
  numbers = get_bus_numbers()
  print(time)
  print(numbers)
  return 0

result = get_result()
print("Result is: " + str(result))
