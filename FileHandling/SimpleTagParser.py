__author__ = 'ManiKanta Kandagatla'

test_cases = ["TagInputData_1.txt","TagInputData_2.txt"]
'''
The input file should of this following format
1. Each line consists of either a tag/tag value/empty line
'''
import re
def parse_file(file_handle):
    start_tag_pattern = re.compile("\[[a-zA-Z]+[0-9]*\]")
    end_tag_pattern = re.compile("\[/[a-zA-Z]+[0-9]*\]")
    tag_list = []
    tag_count = 0
    for line in file_handle.readlines():
        line = line.strip()
        if line !="" :
            if not start_tag_pattern.match(line) == None:
                start_tag = re.sub("\[|\]|\\n","",line)
                tag_list.append(start_tag)
                tag_count = tag_count + 1
            elif not end_tag_pattern.match(line) ==None:
                end_tag = re.sub("\[|\]|\\n|/","",line)
                if end_tag != tag_list[tag_count - 1]:
                    print "**************Parse Error Detected***************"
                    return
                else:
                    tag_list.pop(tag_count - 1)
                    tag_count = tag_count -1
            else:
                print '.'.join(tag_list) + '=' + line.strip()


def run_test_cases():
    for file in test_cases:
        print "Executing parse file: ", file
        with open(file) as file_handle:
            parse_file(file_handle)
        print '\n'

def main():
    run_test_cases()

main()