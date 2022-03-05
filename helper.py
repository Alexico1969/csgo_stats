def fill_till(string, wanted_length):
    output = string
    string_length = len(string)
    spaces_to_add = wanted_length - string_length
    output += spaces_to_add * " "
    return output
