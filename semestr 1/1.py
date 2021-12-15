with open("input.txt", 'r', encoding='utf-8') as input_file, open("output.txt", 'w', encoding='utf-8') as output_file:
    for i in sorted(input_file.read().split('\n')):
        print(i, file=output_file)



