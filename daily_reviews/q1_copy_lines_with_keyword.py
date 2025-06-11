
def copy_lines_with_keyword(filename, keyword):
    try:
        with open(filename, 'r' ) as file:
           file_content = file.read()
    except FileNotFoundError:
        print("File not found!")
        return []

    main_list = file_content.splitlines()
    results = []
    for line in lines: 
        words_in_line = line.split()
        for word in words:
            if keyword == ele:
                results.append(line)
                break
    return results

            
print(copy_lines_with_keyword('testerr.txt', 'data'))






