from helpers import *

# ALL BUS NUMBERS ARE PRIME!
def get_result():
  buses = get_bus_list()
  time = int(buses[0])
  processed_bus_numbers = {int(buses[0])}

  while True:
    time_cache = time
    for bus in buses:
      if bus == 'x':
        time = time +1
        continue
      number = int(bus)
      if time % number == 0:
        if(bus == buses[-1]):
          return time_cache
        time = time +1
        processed_bus_numbers.add(number)
      else:
        step = 1
        for processed_bus_number in processed_bus_numbers:
          step = step * processed_bus_number
        time = time_cache + step
        break
  return 0

result = get_result()
print("Result is: " + str(result))
