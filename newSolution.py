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

    try:
        os.mkdir(firstLetter)
    except:
        pass

    shutil.copy("Template.py", os.path.join(firstLetter, name + ".py"))

    print("All set up, you can find your new file under " + os.path.join(firstLetter, name + ".py"))