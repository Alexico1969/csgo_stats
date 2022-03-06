def fill_till(string, wanted_length):
    string_length = len(string)
    if string_length == 1:
        output = " " + string
        string_length = 2
    else:
        output = string
    spaces_to_add = wanted_length - string_length
    output += spaces_to_add * " "
    return output

