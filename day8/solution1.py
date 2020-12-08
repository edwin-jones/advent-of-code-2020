import helpers

lines = helpers.get_input_as_lines()

def get_result():
    acc = 0
    pc = 0

    previous_lines = []

    while pc not in previous_lines:
        
        line = lines[pc]
        value = line.split(' ')[1]

        if "jmp" in line:
            previous_lines.append(pc)
            pc = pc + int(value)
            continue
        
        if "acc" in line:
            acc = acc + int(value)

        previous_lines.append(pc)
        pc = pc + 1

    return acc

result = get_result()
print("Result is: " + str(result))
