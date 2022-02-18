import os
import shutil
import sys
import re


if __name__ == '__main__':
    assert len(sys.argv) == 2, "1 argument expected, got " + str(len(sys.argv) - 1)
    name = sys.argv[1]
    assert re.match("^[A-Za-z0-9_-]*$", name), "name should contains only  letters and numbers"
    if name[0].islower():
        name = name[0].upper() + name[1:]

    firstLetter = name[:1]

    if firstLetter.isdigit():
        firstLetter = "0-9"

    path = os.path.join(firstLetter, name + ".py")

    try:
        os.mkdir(firstLetter)
    except:
        pass

    shutil.copy("Template.py", path)

    # Read in the file
    with open(path, 'r') as file:
        file_data = file.read()

    # Replace the target string
    file_data = file_data.replace('Template', name)
    file_data = file_data.replace('template', name)

    # Write the file out again
    with open(path, 'w') as file:
        file.write(file_data)

    print("All set up, you can find your new file under " + path)