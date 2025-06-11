from contextlib import contextmanager #ok does the with statement not work without this import?


#creating a function to read the text file
def copy_lines_with_keyword(filename, keyword):
    with open(filename, 'r' ) as file:
        data = file.read()

        main_list = data.splitlines()
        results = []
        for line in main_list: 
            new_line = str(line)
            words = new_line.split()
            for ele in words:
                if keyword == ele:
                    results.append(line)
                    break
    return results

            
print(copy_lines_with_keyword('tester.txt', 'DaTA'))






