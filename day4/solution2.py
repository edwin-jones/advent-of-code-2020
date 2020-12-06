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
            
            else:
                tokens = batch.replace('\n', ' ').split(' ')

                for token in tokens:
                    if field not in token :
                        continue

                    value = token.replace(field, '')

                    if field == "byr:":
                        if int(value) < 1920 or int(value) > 2002:
                            error = True
                            break

                    
                    if field == "iyr:":
                        if int(value) < 2010 or int(value) > 2020:
                            error = True
                            break

                    if field == "eyr:":
                        if int(value) < 2020 or int(value) > 2030:
                            error = True
                            break
                    
                    if field == "pid:":
                        if len(value) != 9 or value.isdigit == False:
                            error = True
                            break
        
        if(error == False):
            count = count + 1
    
    return count

print(len(batches))
result = get_result()
print("Result is: " + str(result))
