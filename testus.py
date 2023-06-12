def is_palindrom(string):
    string_rev=string[::-1]
    if string == string_rev:
        print('True')
    else:
        print('False')
