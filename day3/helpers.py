import os

def set_directory():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

def get_input_as_lines():
    lines = []

    with open('./input.txt','r') as input:
        for line in input:
            lines.append(line)

    return lines