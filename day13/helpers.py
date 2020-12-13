import os

def set_directory():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

def get_input_as_lines():
    set_directory()
    lines = []

    with open('./input.txt','r') as input:
        for line in input:
            lines.append(line.replace('\n', ''))

    return lines


def get_departure_time():
  lines = get_input_as_lines()
  line = lines[0].replace('\n', '')
  return int(line)

def get_bus_numbers():
  lines = get_input_as_lines()
  numbers = lines[1].replace('\n', '').split(',')
  result = []
  for number in numbers:
    if number == 'x':
      continue
    result.append(int(number))
  result.sort()
  return result