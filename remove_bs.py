import json

with open('story_small.json') as f:
    data = json.load(f)

print(data["Chapter_1"])

# json_string = data.keys()
# new_clear = json_string.replace("\\", "")
# print(new_clear)
