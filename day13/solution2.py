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

  buses.reverse()
  time = int(buses[0])
  step = time

  while True:
    time_cache = time
    print(str(time))
    for bus in buses:
      if bus == 'x':
        time = time - 1
        continue
      number = int(bus)
      if time % number == 0:
        print(f"Bus:{bus}, Time:{time}")
        if(bus == buses[-1]):
          return time
        time = time -1
      else:
        time = time_cache + step
        break


  return 0

result = get_result()
print("Result is: " + str(result))
