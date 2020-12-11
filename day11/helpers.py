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

def get_input_as_batches():
    set_directory()
    batches = []

    with open('./input.txt','r') as input:
        current_batch = ""
        for line in input:
            if(line!= "\n"):
                current_batch = current_batch + line.replace('\n', '')
            else:
                batches.append(current_batch)
                current_batch = ""
        
        batches.append(current_batch)

    return batches

def get_input_as_batches_of_lines():
    set_directory()
    batches = []

    with open('./input.txt','r') as input:
        current_batch = []
        for line in input:
            if(line!= "\n"):
                current_batch.append(line.replace('\n', ''))
            else:
                batches.append(current_batch)
                current_batch = []
        
        batches.append(current_batch)

    return batches

def get_input_as_numbers():
    set_directory()
    numbers = []

    with open('./input.txt','r') as input:
        for line in input:
            numbers.append(int(line))

    return numbers