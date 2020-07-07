# Author: Jamal Huraibi, fh1328
# Assignment 4
# Question 1
# Note: Referenced datetime information from docs.python.org
#                now():     https://docs.python.org/3/library/datetime.html#datetime.datetime.now
#           strftime():     https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

import datetime


# TODO: Determine how to reference file data
# e.g. Load/Read file each time or keep local copy in a str var?
# TODO: Change self.file_ref to a method-only scope?
class File:
    def __init__(self, initial_file_name, initial_content=" "):
        self.file_number = None
        self.file_name = initial_file_name
        self.file_owner = " "
        self.time_modified = None
        self.content = initial_content
        self.date_last_modified = " "
        self.__update_file_counter()
        self.__update_date_modified()                                           # Update the time last modified
        
        self.file_ref = None    # TODO: Update according to future method of handling file opening
    
    
    @staticmethod
    def __update_file_counter():
        """Updates the file-number counter."""
        pass
    
    
    def get_number(self):
        """Returns the file number."""
        return self.file_number
        
        
    def get_name(self):
        """Returns the file name."""
        return self.file_name
    
    
    def set_owner(self, owner_name):
        """Updates the name of the file owner."""
        self.file_owner = owner_name
        self.__update_date_modified()                                           # Update the time last modified
        
        
    def get_owner(self):
        """Returns the name of the file owner (if one was set). Otherwise, returns an alert that none was set."""
        if self.file_owner == " ":
            return "[No Owner Has Been Set]"                                    # Handle file having no owner
        else:
            return self.file_owner                                              # If has owner, return the name
        
        
    def __update_date_modified(self):
        """Updates the last date and time file was modified (i.e. time when method was called)."""
        self.date_last_modified = datetime.datetime.now()
        
        
    def get_date(self):
        """Returns the last date and time file was modified."""
        return self.date_last_modified
    
    # TODO: Instructions don't give a date format to use
    def print_date_style_1(self):
        """Prints date-modified as HH:MM:SS on MM/DD/YYYY"""
        date_ref = self.get_date()                                              # Establish a reference to the datetime
        time = date_ref.strftime("%X")                                          # HH:MM:SS
        date = date_ref.strftime("%x")                                          # MM/DD/YYYY
        
        print("Date Last Modified: {} on {}".format(time, date))                # Print date as "HH:MM:SS on MM/DD/YYYY"
        
        
    def add_line(self, text_to_add):
        """Adds a new line to the end of file."""
        self.file_ref = open(self.file_name, 'a')                               # Open the file in append mode
        
        self.file_ref.write(text_to_add)                                        # Append the new data
        
        self.file_ref.close()                                                   # Close the file
        self.__update_date_modified()                                           # Update the time last modified
        
    
    def delete_line(self, line_number):
        """Deletes a specific line from file."""
        self.file_ref = open(self.file_name, 'rw')                              # Open the file in read/write mode
        
        content = self.file.read()                                              # Store file contents as single string
        content_by_lines = content.split('\n')                                  # Delimit by new line
        content_by_lines[line_number] = ""                                      # Erase content at provided line number
        
        rebuilt_content = "".join(content_by_lines)                             # Convert List back into single string
        
        self.file_ref.write(rebuilt_content)                                    # Write the updated content to file
        
        self.file.close()                                                       # Close the file
        self.__update_date_modified()                                           # Update the time last modified
        
    # TODO: Clarify if printing or just return raw content
    def get_content(self):
        """Fetches the entire content of the file and returns it."""
        self.file_ref = open(self.file_name, 'r')                               # Open the file in read mode
        all_content = self.file_ref.read()                                      # Read-in data as single string
        
        print("File Content: \n{}".format(all_content))                         # Print header followed by file content
        
        self.file_ref.close()                                                   # Close the file
        
        
    def set_content(self, new_content):
        """Changes the content of the text file, overwriting any existing text."""
        self.file_ref = open(self.file_name, 'w')                               # Open the file in read/write mode
        self.file_ref.write(new_content)                                        # Write the new content
        self.file_ref.close()                                                   # Close the file
        
        self.__update_date_modified()                                           # Update the time last modified
        
        
    def has_word(self, word_to_find):
        """Checks if the file has a specific word in it. Returns true if the word is found, otherwise returns false."""
        self.__update_local_content()
        return word_to_find in self.content
    
    # TODO: Add error handling
    def __update_local_content(self):
        self.file = open(self.file_name, 'r')                                   # Open the file in read mode
        self.content = self.file.read()                                         # Store file contents as single string
        self.file.close()                                                       # Close the file
    
    # TODO: Make sure other file content is str (check: .write() cannot do numbers, p. 119)
    def add_from(self, other_file_content):
        """Adds the content of the other file to the end of the current file."""
        self.file_ref = open(self.file_name, 'a')                               # Open the file in append mode
        
        self.file_ref.write(other_file_content)                                 # Append the data from other file
        
        self.file_ref.close()                                                   # Close the file
        self.__update_date_modified()                                           # Update the time last modified
    
    # TODO: Make sure unwanted items are not being counted
    def count_words(self):
        """Counts the number of words in a file and returns it."""
        self.file_ref = open(self.file_name, 'a')                               # Open the file in append mode
        raw_content = self.file_ref.read()                                      # Store content as single string
        words = raw_content.split()                                             # Separate into individual words

        self.file_ref.close()                                                   # Close the file
        
        return len(words)                                                       # len will num of indiv. words
    
    
    def replace(self, target, replacement):
        """Replaces (target: str) with (replacement: str) everywhere in the file."""
        self.file_ref = open(self.file_name, 'rw')                              # Open the file in read/write mode
        raw_content = self.file_ref.read()                                      # Store content as single string
        
        updated_content = raw_content.replace(target, replacement)              # Replace occurences of target substring
        
        self.file_ref.write(updated_content)                                    # Write updated content to file

        self.file_ref.close()                                                   # Close the file
        self.__update_date_modified()                                           # Update the time last modified
    
    
    def open_file(self):
        self.file_ref = open(self.file_name, 'r')                               # Open the file in read mode
        # Don't close yet, the calling method will access the file
        # !! Critical: Ensure calling method closes file
    
    # TODO: Refactor name to better illustrate purpose
    @staticmethod
    def __generate_file_name(name):
        """Checks if a file already exists with the intended file-name.
        If no: returns the available file name.
        If yes: Concatenate a modifier to the file name, re-check with the modified name.
        """
        import os
        file_exists = os.path.exists(name)
        modifier = 1
        
        while file_exists:
            name = "{}-{}.txt".format(name, modifier)
            file_exists = os.path.exists(name)
            modifier = modifier + 1
        
        return name


if __name__ == '__main__':
    # A = File("test")
    # B = File("test")
    # C = File("test")
    #
    # print("A File Number: {}".format(A.get_number()))
    # print("B File Number: {}".format(B.get_number()))
    # print("C File Number: {}".format(C.get_number()))
    #
    # print("C File Date: {}".format(C.get_date()))
    # C.print_date_style_1()
    
    A = File("test1", "This is a file with some text")
    B = File("test2")
    C = File("test1", "This is another file with some text")
    D = File("test2")
    
    C.set_owner("John Doe")
    D.set_owner("Runtao Zhu")
    
    print(A.get_owner())
    print(D.get_owner())
    
    D.set_content("This is a new content")
    D.add_from(A)
    D.get_date()
    B.add_line("Hello World!")
    B.add_line("This is a new line!")
    B.delete_line(1)
    print(A)
    
    # replaces the word "this" with the word "that" everywhere in the file.
    A.replace("this","that")
    
    print(A.getContent())

    # returns true if the file contains the word this
    B.hasWord("World")

    # The content of A and B are added together and written into a new file E.
    E = A + B

    # returns true, if the number of words in A is greater than the number of words in B
    A > B