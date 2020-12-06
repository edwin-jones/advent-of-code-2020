import helpers

helpers.set_directory()
batches = helpers.get_input_as_batches()

fields = [
"byr:",
"iyr:", 
"eyr:",
"hgt:", 
"hcl:",
"ecl:", 
"pid:"
]

def get_result():
    count = 0
    x = 0
    error = False

    for batch in batches:
        error = False
        for field in fields:
            if field not in batch:
                error = True
                break
        
        if(error == False):
            count = count + 1
    
    return count

print(len(batches))
result = get_result()
print("Result is: " + str(result))
