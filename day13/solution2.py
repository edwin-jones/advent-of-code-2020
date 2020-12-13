from helpers import *

def check_prev_bus_time(bus_num, previous_time, gap):
  result = 0
  while result < previous_time:
    result += bus_num
  if result - gap == previous_time:
    return True
  else:
    return False

def get_result():
  buses = get_bus_list()

  buses
  time = int(buses[0])
  step = time

  lcms = {time}
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
        lcms.add(number)
      else:
        test = 1
        for num in lcms:
          test = test * int(num)
        step = test
        time = time_cache + step
        break
  return 0

result = get_result()
print("Result is: " + str(result))
