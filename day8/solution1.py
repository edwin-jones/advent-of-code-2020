import helpers

lines = helpers.get_input_as_lines()

def get_result():
    acc = 0
    pc = 0

    previous_lines = []

    while pc not in previous_lines:
        
        line = lines[pc]
        tokens = line.split(' ')

        if "jmp" in line:
            previous_lines.append(pc)
            pc = pc + int(tokens[1])
            continue
        
        if "acc" in line:
            tokens = line.split(' ')
            acc = acc + int(tokens[1])

        previous_lines.append(pc)
        pc = pc + 1

    return acc

result = get_result()
print("Result is: " + str(result))
