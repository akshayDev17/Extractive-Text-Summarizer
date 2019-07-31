""" Module created to remove whitespace characters """

def clean_up(input_string):

    """ Replaces all whitespace characters except the space after any
    punctuation mark """

    table = {ord('\f') : ' ', ord('\t') : ' ', ord('\n') : ' ', ord('\r') : None}
    return input_string.translate(table)
