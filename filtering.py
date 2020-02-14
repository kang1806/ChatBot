import json
import yaml

with open('output.json') as json_file:
    lines = []
    for line in json_file:
        lines.append(line[50:-3])

    with open (r'C:\Users\wenka_000\Desktop\ChatBot\TestChatBot\testing.yml', 'w') as file:
        documents = yaml.dump(lines, file)
