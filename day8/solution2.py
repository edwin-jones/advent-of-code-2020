import helpers
import time

lines = helpers.get_input_as_lines()

def get_result():


    for idx, val in enumerate(lines):
        start_time = time.time()

        acc = 0
        pc = 0

        # limit cycles to ten seconds
        while time.time() - start_time < 10_000:
            
            line = lines[pc]

            tokens = line.split(' ')

            if "jmp" in line:
                pc = pc + int(tokens[1])
                continue
            
            if "acc" in line:
                tokens = line.split(' ')
                acc = acc + int(tokens[1])

            pc = pc + 1

            if pc >= len(lines):
                return acc

    raise Exception("no results found")

result = get_result()
print("Result is: " + str(result))
