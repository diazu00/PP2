with open('example.txt', 'r') as old_file:
    with open('e_new.txt', 'w') as new_file:
        new_file.write(old_file.read())