def fill_till(string, wanted_length):

    output = string
    string_length = len(string)
    if string_length == 1:
        string = " " + string
    spaces_to_add = wanted_length - string_length
    output += spaces_to_add * " "
    return output

