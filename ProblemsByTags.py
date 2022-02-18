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
                if str(t) not in Tags:
                    Tags[str(t)] = [filename.split(".py")[0]]
                else:
                    Tags[str(t)].append(filename.split(".py")[0])

    with open("ProblemsByTags.json", "w") as f:
        f.write(json.dumps(Tags))