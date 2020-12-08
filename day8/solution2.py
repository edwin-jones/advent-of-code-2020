import helpers
import time

lines = helpers.get_input_as_lines()

def get_result():


    for idx, val in enumerate(lines):
        print(f"checking line {idx} with value: '{val}'")
        start_time = time.time()

        modified_lines = lines.copy()

        if "nop" in val:
            modified_lines[idx] = modified_lines[idx].replace("nop", "jmp")
        
        if "jmp" in val:
            modified_lines[idx] = modified_lines[idx].replace("jmp", "nop")

        acc = 0
        pc = 0

        ops = 0

        # limit cycles to n seconds
        while True:

            if pc >= len(modified_lines):
                return acc

            ops = ops + 1
            elapsed  = time.time() - start_time
            if ops > 1000:
                print(f"Ops: {ops}")
                break

            print(f"pc: {pc}")
            line = modified_lines[pc]

            tokens = line.split(' ')

            if "jmp" in line:
                pc = pc + int(tokens[1])
                continue
            
            if "acc" in line:
                tokens = line.split(' ')
                acc = acc + int(tokens[1])

            pc = pc + 1

    raise Exception("no results found")

result = get_result()
print("Result is: " + str(result))
