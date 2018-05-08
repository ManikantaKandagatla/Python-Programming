__author__ = 'ManiKanta Kandagatla'

import os
test_cases = ["E:\\spring-security-hibernate-annotation\\src"]

def print_directory_contents(path,partial_path,level):
    try:
        if level == 0:
            print path
        else:
            print " "*(level),"+-",partial_path
        for content in os.listdir(path):
            content_path = os.path.join(path,content)
            if os.path.isdir(content_path) == True:
                print_directory_contents(content_path,content,level + 1)
            else:
                print " "*(level),"|","-",content
    except WindowsError:
        pass

def run_test_cases():
    for path in test_cases:
        print '#################################'
        print 'Path: ', path
        print_directory_contents(path,"",0)

run_test_cases()