import json
import yaml

open(r'C:\Users\wenka_000\Anaconda3\envs\chat\Lib\site-packages\chatterbot_corpus\data\training\trained.yml', "w").close()
with open('output.json') as json_file:
    lines = []
    for line in json_file:
        lines.append(line[50:-3])

    with open (r'C:\Users\wenka_000\Anaconda3\envs\chat\Lib\site-packages\chatterbot_corpus\data\training\trained.yml', 'w') as file:
        yaml.dump(lines, file)
        

format_line = 0
num_lines = sum(1 for line in open(r'C:\Users\wenka_000\Anaconda3\envs\chat\Lib\site-packages\chatterbot_corpus\data\training\trained.yml'))
with open (r'C:\Users\wenka_000\Anaconda3\envs\chat\Lib\site-packages\chatterbot_corpus\data\training\trained.yml', 'r') as file:
    data = file.readlines()
    while format_line < num_lines:
        if format_line == 0:
            data[format_line] = "- " + data[format_line]
            format_line = format_line + 1
        else:
            data[format_line] = data[format_line][4:]
            data[format_line] = "  - " + data[format_line]
            format_line = format_line + 1
with open (r'C:\Users\wenka_000\Anaconda3\envs\chat\Lib\site-packages\chatterbot_corpus\data\training\trained.yml', 'w') as file:
    file.write("categories:\n")
    file.write("- trained\n")
    file.write("conversations:\n")
    file.writelines(data)
    