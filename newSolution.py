import os
import shutil
import sys
import re


if __name__ == '__main__':
    assert len(sys.argv) == 2, "1 argument expected, got " + str(len(sys.argv) - 1)
    name = sys.argv[1]
    assert re.match("^[A-Za-z][A-Za-z0-9_-]*$", name), "name should start with a letter, and contains only letters and numbers"
    if name[0].islower():
        name = name[0].upper() + name[1:]

    firstLetter = name[:1]
    dirPath = os.path.join("Solutions", firstLetter)
    path = os.path.join("Solutions", firstLetter, name + ".py")

    try:
        os.mkdir(dirPath)
        open(os.path.join(dirPath,"__init__.py"), "w").close()
    except:
        pass

    shutil.copy("Template.py", path)

    # Read in the file
    with open(path, 'r') as file:
        file_data = file.read()

    # Replace the target string
    file_data = file_data.replace('Template', name)
    file_data = file_data.replace('template', name[0].lower() + name[1:])

    # Write the file out again
    with open(path, 'w') as file:
        file.write(file_data)

    print("All set up, you can find your new file under " + path)