# Thanh Vu (17627579) and Julie Huynh (46376331). Lab Section 4.

import os.path
import os
import shutil
from datetime import date



# Step1: Asking user for input repeatedly for the path to directory
def user_interface():

    while True:
        file_path= input('Please Enter The Path To A Directory or Type Exit to quit the program: ').strip()
        if file_path == 'exit' or file_path == 'Exit':
            quit()

        try:
            #access the directory and get the list of all the files in that directory if directory existed
            # recursion of subdirectories inside directory:

            allfiles_list = accessing_subdirectory(file_path)
            

            # asking user which ways they want to search for their files repeatedly
            while True:
                action_to_search_file= str(input('''
How would you like to search?
name  : Search by Name
type  : Search by Name Ending (.doc, .txt., etc)
size  : Search by File Size in Bytes

''')).lower()

            # have an initilal list called interesting_files. Through each search function, return a list of interesting files
            # from each search function and then append each of them to the initial list of interesting files.
                if action_to_search_file == 'name':
                    interesting_file = search_files_name(allfiles_list,file_path)
                    break
                elif action_to_search_file == 'type':
                    interesting_file = search_files_name_ending(allfiles_list,file_path)
                    break
                elif action_to_search_file == 'size':
                    interesting_file = search_files_size(allfiles_list)
                    break

                else:
                    # print error message and ask the user to retype the command if command is invalid
                    print("Command is invalid. Please Enter a valid search characteristic method.")

            while True:
                # asking the user for the action to take one of the 4 actions:
                print_path_only(interesting_file,allfiles_list)
                user_input_action = str(input('''

Please choose one of the five following actions:

A: Print Path
B: Print first line of text
C: Copy File
D: Touch File

'''))
                if user_input_action == 'A':
                    # access the print path only function
                    print_path_only(interesting_file,allfiles_list)

                    break
                elif user_input_action == 'B':
                    # access the print 1st line function
                    print_1st_line_text(interesting_file,allfiles_list)

                    break
                elif user_input_action == 'C':
                    #access the copy file function
                    copy_file(interesting_file,allfiles_list)

                    break
                elif user_input_action == 'D':
                    #access the touch file function
                    touch_file(interesting_file,allfiles_list)

                    break
                else:
                    print("Action selected is not valid. Please choose another action")

        except:
            #print out error message and tell user to search for another directory if directory is not there
            print("File Path is not existed. Please Enter Another Directory Path")



# Step2: After having the list of all files in the directory, access the files in 3 different ways

# Ask the user which way they want to get their files:


def search_files_name(allfile_list:'list of files',directory_path:'file_path'):
    # Name file exactly matched the user input name and append those files to interest_file list
    interest_file=[]
    while True:
        user_file_inputname= str(input('Please Enter the exact file name to search: '))

        # ilerate through each file in that directory:
        for file in allfile_list:
            if file == user_file_inputname:
                interest_file.append(user_file_inputname)
        if interest_file != []:
            break
        if user_file_inputname not in allfile_list:
            print("File's name is not in the directory. Please enter another file name to search")

    print(interest_file)
    return interest_file



def search_files_name_ending(allfile_list:'list of files',directory_path: 'file path'):
    # Search file by their extension name and then append it to the list called interest_file
    interest_file=[]
    while True:
        user_file_input_endstring= str(input('Please Enter The Type of File: '))
        each_file_endstring_list=[]

        for file in allfile_list:
            each_file_endstring = os.path.splitext(os.path.join(directory_path,file))[1]
            each_file_endstring_list.append(each_file_endstring)

            if user_file_input_endstring == each_file_endstring:
                interest_file.append(file)
        if interest_file != []:
            break
        if user_file_input_endstring not in each_file_endstring_list:
            print("File's name ending does not match any ending in the file in this directory. Please enter another file name's ending to search")

    
    return interest_file


def search_files_size(all_path_and_files_list:'list of files and path'):
    # files who size exceeds the specified threshold value
    interest_file=[]

    interest_path=[]
    while True:
        try:
            threshold_value= int(input('Please Enter The Threshold Value of the file: '))
            for file in all_path_and_files_list:
                if os.path.exists(file):
                    interest_path.append(file)

            for path in interest_path:
                for each in all_path_and_files_list:
                    test_path= os.path.join(path,each)
                    if os.path.exists(test_path) == True:
                        file_size = os.path.getsize(test_path) #get size of each file in the list

                        if file_size >= threshold_value and '.' in each:
                            interest_file.append(each)
            break
        except:
            print("You entered an invalid threshold value. Please Enter another threshold value to search")

    
    return interest_file

def print_path_only(interesting_file:'desired file',all_path_and_files_list:'list of path and files'):
    # Print Path that lead to the file
    interesting_file= set(interesting_file)
    for file in interesting_file:
        for element in all_path_and_files_list:
            test_path = os.path.join(element,file)
            if os.path.exists(test_path):
                print(test_path)


def print_1st_line_text(interesting_file:'desired file',all_path_and_files_list:'list of path and files'):
    # Access interesting files and print out the 1st line of text if files are text documents. Otherwise,
    # it will take the user back to the path input step
    interesting_file= set(interesting_file)
    try:
        for file in interesting_file:
            for element in all_path_and_files_list:
                test_path= os.path.join(element,file)
                if os.path.exists(test_path):
                    the_file= open(test_path,'r')
                    first_text= the_file.readline()
                    print(first_text)


    except:
        print("some of the files are not text files and cannot be opened to read.")


def copy_file(interesting_file:'desired file',all_path_and_files_list:'list of path and files'):

    for file in interesting_file:
        for element in all_path_and_files_list:
            test_path= os.path.join(element,file)
            if os.path.exists(test_path):
                (file_dir, file_name)= os.path.split(test_path)
                copy_file_name = file_name + '.dub'
                new_copy_file_path= os.path.join(file_dir,copy_file_name)
                shutil.copy(test_path,new_copy_file_path)


def touch_file(interesting_file:'desired file',all_path_and_files_list:'list of path and files'):
    for file in interesting_file:
        for element in all_path_and_files_list:
            test_path= os.path.join(element,file)
            if os.path.exists(test_path):
                os.utime(test_path)

def accessing_subdirectory(file_path: 'file_path'):
    file_list=[]
    file_abs_path=[]
    file_abs_path.append(file_path)
    for each_element in os.listdir(file_path):

        if '.' not in each_element:

            new_folder_path = os.path.abspath(os.path.join(file_path, each_element))

            if os.path.exists(new_folder_path):
                for each_file in accessing_subdirectory(new_folder_path):
                    file_list.append(each_file)

        else:
            file_list.append(each_element)

    file_list += file_abs_path
    return(file_list)


if __name__ == '__main__':
    user_interface()


