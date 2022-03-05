from data import data_str

output = ""
indentation = ""

for e in data_str:
    '''
    if e=="{":
        output += "{" + indentation
    else:
        output += e
    '''

    output += e

print(output)