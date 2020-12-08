import helpers

lines = helpers.get_input_as_lines()

def get_result():

    for idx, val in enumerate(lines):

        modified_lines = lines.copy()

        if "nop" in val:
            modified_lines[idx] = modified_lines[idx].replace("nop", "jmp")
        
        if "jmp" in val:
            modified_lines[idx] = modified_lines[idx].replace("jmp", "nop")

        acc = 0
        pc = 0
        previous_lines = []

        while pc not in previous_lines:

            if pc >= len(modified_lines):
                return acc

            previous_lines.append(pc)

            line = modified_lines[pc]

            value = line.split(' ')[1]

            if "jmp" in line:
                pc = pc + int(value)
                continue
            
            if "acc" in line:
                tokens = line.split(' ')
                acc = acc + int(value)

            pc = pc + 1

    raise Exception("no results found")

result = get_result()
print("Result is: " + str(result))
