import json
import yaml

with open('output.json') as json_file:
    lines = []
    for line in json_file:
        lines.append(line[50:-3])

    with open (r'C:\Users\wenka_000\Desktop\ChatBot\TestChatBot\trained.yml', 'w') as file:
        file.write("categories:\n")
        file.write("- trained\n")
        file.write("conversations:\n")
        file.write("- ")
        yaml.dump(lines, file)
