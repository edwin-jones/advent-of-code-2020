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
  numbers = lines[1].replace('\n', '').replace('x','').split(',')
  return numbers