import os
import importlib
import json

if __name__ == '__main__':
    directory = os.path.join("Solutions")
    Tags = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            path = os.path.join(root, filename)
            if "__" in path:
                continue
            tags = importlib.import_module(path.replace("\\", ".").split(".py")[0]).Solution().getTags()
            for t in tags:
                tag_type, tag_val = str(t).split(".")
                if tag_type not in Tags:
                    Tags[tag_type] = {}
                if tag_val not in Tags[tag_type]:
                    Tags[tag_type][tag_val] = [filename.split(".py")[0]]
                else:
                    Tags[tag_type][tag_val].append(filename.split(".py")[0])

    with open("ProblemsByTags.json", "w") as f:
        f.write(json.dumps(Tags, indent=4, sort_keys=True))