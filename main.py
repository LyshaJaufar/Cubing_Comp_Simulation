import json


events = ['222', '333', '444', '555', '666', '777',
          '333oh', 'clock', 'minx', 'pyram', 'skewb', 'sq1']
cubers = []

# Opening JSON file
f = open('cubers.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
# for i in data['results']:
# print(i)

for event in data['results']:

    for cuber in event:
        print(cuber['event'])


# Closing file
f.close()
