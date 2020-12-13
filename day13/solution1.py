from helpers import *

def get_result():
  time = get_departure_time()
  numbers = get_bus_numbers()
  results = {}

  for number in numbers:
    accumulator = 0
    while True:
      accumulator += number
      if accumulator > time:
        break

    diff = accumulator - time
    results[diff] = number

    shortest_wait = 2**32
    for key in results.keys():
      if key < shortest_wait:
        shortest_wait = key

    bus = results[shortest_wait]
  print(f"RESULT: bus = {bus}, shortest wait:{shortest_wait}")
  return shortest_wait * bus

result = get_result()
print("Result is: " + str(result))
