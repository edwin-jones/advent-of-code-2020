import helpers

lines = helpers.get_input_as_lines()

def get_result():
    target_color = "shiny gold"
    colors = [target_color]
    processing = True

    while(processing):
        processing = False
        for line in lines:
            if "no other bags" in line:
                continue
            
            pos = line.index(' ')
            current_color = line[:line.index(' ', pos + 1)]
            if current_color == target_color:
                continue

            if any(color in line for color in colors):
                if(current_color not in colors):
                    colors.append(current_color)
                    processing = True
    
    return len(colors) - 1

result = get_result()
print("Result is: " + str(result))
