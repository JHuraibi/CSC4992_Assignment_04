# Author: Jamal Huraibi, fh1328
# Assignment 4
# Question 1
# Note: Referenced datetime information from docs.python.org
#                now():     https://docs.python.org/3/library/datetime.html#datetime.datetime.now
#           strftime():     https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

import datetime


# TODO: is file counter working?
class File:
    file_counter = 1
    
    def __init__(self, initial_file_name, initial_content=" "):
        self.file_number = File.file_counter
        self.file_name = None
        self.file_owner = " "
        self.time_modified = None
        self.date_last_modified = " "
        self._generate_file_name(initial_file_name)                             # Set/generate and set file name
        self._create_file()                                                     # Create file with the generated name
        self._write_initial_content(initial_content)                            # Write initial content (if provided)
        self._update_date_modified()                                            # Set the last-modified date/time
        File.file_counter = File.file_counter + 1                               # Increment the file counter
    
    
    def __add__(self, other):
        """Returns a new file that contains the content of the current File instance and passed-in File instance.
        A default name is assigned as well."""
        new_content = self.get_content() + other.get_content()
        new_file = File("NewFile", new_content)
        
        return new_file

    
    def __lt__(self, other):
        """Returns true if the number of words of calling File is LESS than (other: File)"""
        length = self.count_words()                                             # Number of words of calling File
        length_of_other = other.count_words()                                   # Number of words of passed-in File
        
        return length < length_of_other


    def __gt__(self, other):
        """Returns true if the number of words of calling File is GREATER than (other: File)"""
        length = self.count_words()                                             # Number of words of calling File
        length_of_other = other.count_words()                                   # Number of words of passed-in File
        
        return length > length_of_other


    def __str__(self):
        """Returns the string representation of File objects in the format provided by assignment instructions.
        Format: file number, file name, file owner, time date file was last modified, number words in the file.
        """
        return str(
            "File Number:           {}\n".format(self.file_number) +
            "File Name:             {}\n".format(self.file_name) +
            "File Owner:            {}\n".format(self.get_owner()) +
            "Date Last Modified:    {}\n".format(self.get_date()) +
            "Number of Words:       {}\n".format(self.count_words())
        )
    
        
    def _generate_file_name(self, name):
        """Checks if a file with the intended file-name already exists.
        If no: returns the available file name.
        If yes: Concatenate a modifier to the file name, re-check with the modified name.
        Value of variable "name" is never altered.
        """
        import os
        
        possible_name = "{}.txt".format(name)                                   # Unaltered name passed to __init__

        modifier = 1                                                            # Set the file name modifier
        while os.path.exists(possible_name):
            print("File with name [{}] already exists.".format(possible_name))
            possible_name = "{}-{}.txt".format(name, modifier)                  # Append the modifier to the name
            modifier = int(modifier) + 1                                        # Increment the modifier
        
        self.file_name = possible_name                                          # Store the file name
    
    
    def _create_file(self):
        """Creates a file with the name set/generated by _generate_file_name()"""
        open(self.file_name, "x")                                               # Create the file
        print("File created with name [ {} ].".format(self.file_name))          # Confirmation of the file created
        
        
    def _write_initial_content(self, initial_content):
        import os
        
        if not os.path.exists(self.file_name):
            print("Error opening file to write initial content")
            return None
        
        file_ref = open(self.file_name, "w")                                    # Open the just-recently created file
        file_ref.write(initial_content)                                         # Write the initial content to the file
        file_ref.close()                                                        # Close the file
    
    
    def get_number(self):
        """Returns the file number."""
        return self.file_number
        
        
    def get_name(self):
        """Returns the file name."""
        return self.file_name
    
    
    def set_owner(self, owner_name):
        """Updates the name of the file owner."""
        self.file_owner = owner_name                                            # Save the owner's name
        self._update_date_modified()                                            # Update the time last modified
        
        
    def get_owner(self):
        """Returns the name of the file owner (if one was set). Otherwise, returns an alert that none was set."""
        if self.file_owner == " ":
            return "[No Owner Has Been Set]"                                    # Handle file having no owner
        else:
            return self.file_owner                                              # If it has an owner, return the name
        
        
    def _update_date_modified(self):
        """Updates the last date and time file was modified (i.e. time when method was called)."""
        self.date_last_modified = datetime.datetime.now()                       # Record the current date and time
        
        
    def get_date(self):
        """Returns the last date and time file was modified."""
        return self.date_last_modified                                          # Return the un modified date/time
    
    
    def print_date_style_1(self):
        """Prints date-modified as HH:MM:SS on MM/DD/YYYY"""
        date_ref = self.get_date()                                              # Establish a reference to the datetime
        time = date_ref.strftime("%X")                                          # HH:MM:SS
        date = date_ref.strftime("%x")                                          # MM/DD/YYYY
        
        print("Date Last Modified: {} on {}".format(time, date))                # Print date as "HH:MM:SS on MM/DD/YYYY"

    
    def add_line(self, text_to_add):
        """Adds a new line to the end of file."""
        file_ref = open(self.file_name, 'a')                                    # Open the file in append mode
        
        file_ref.write('\n' + text_to_add)                                      # Append the new data
        
        file_ref.close()                                                        # Close the file
        self._update_date_modified()                                            # Update the time last modified
    
    
    def delete_line(self, line_number):
        """Deletes a specific line from file."""
        
        file_ref = open(self.file_name, 'r+')                                   # Open the file in read/write mode
        
        content = file_ref.read()                                               # Store file contents as single string
        content_by_lines = content.split('\n')                                  # Delimit by new line
        num_of_lines = len(content_by_lines)                                    # Record how many lines there are
        
        if line_number < 1:
            print("Line number must be 1 or greater")                           # Invalid line number entered
            return None
        elif (line_number - 1) > num_of_lines:                                  # (Minus 1 for index-based)
            print("There are only {} lines".format(num_of_lines))               # Line to erase doesn't exist
            return None
        
        removed_line = content_by_lines.pop(line_number - 1)                    # Remove content at intended line number
        print("Removing line {}".format(line_number))                           # Confirmation of line removed
        print("Content that was removed: {}".format(removed_line))              # Confirmation of what was removed
        
        rebuilt_content = "".join(content_by_lines)                             # Convert List back into single string
        file_ref.write(rebuilt_content)                                         # Write the updated content to file
        
        file_ref.close()                                                        # Close the file
        self._update_date_modified()                                            # Update the time last modified
        
    
    def get_content(self):
        """Fetches the entire content of the file and returns it."""
        file_ref = open(self.file_name, 'r')                                    # Open the file in read mode
        all_content = file_ref.read()                                           # Read-in data as single string
        
        file_ref.close()                                                        # Close the file
        
        return all_content                                                      # Return the content
        
        
    def set_content(self, new_content):
        """Changes the content of the text file, overwriting any existing text."""
        file_ref = open(self.file_name, 'w')                                    # Open the file in read/write mode
        file_ref.write(new_content)                                             # Write the new content
        file_ref.close()                                                        # Close the file
        
        self._update_date_modified()                                            # Update the time last modified
        
        
    def has_word(self, word_to_find):
        """Checks if the file has a specific word in it. Returns true if the word is found, otherwise returns false."""
        file_ref = open(self.file_name, 'r')                                    # Open the file in read mode
        raw_content = file_ref.read()                                           # Store content as single string
        words = raw_content.split()                                             # Separate into individual words
        
        return word_to_find in words                                            # Is the word in the List of words?
    
    
    def add_from(self, other_file):
        """Adds the content of the other file to the end of the current file."""
        file_ref = open(self.file_name, 'a')                                    # Open the file in append mode
        other_file_content = other_file.get_content()                           # Load the contents of the other file
        
        file_ref.write('\n' + other_file_content)                               # Append the data from the other file
        
        file_ref.close()                                                        # Close the file
        self._update_date_modified()                                            # Update the time last modified
    
    
    def count_words(self):
        """Counts the number of words in a file and returns it."""
        words = self._convert_file_to_list(self.file_name)

        return len(words)                                                       # List length == num of indiv. words
    
    
    def replace(self, target, replacement):
        """Replaces (target: str) with (replacement: str) everywhere in the file. Target IS case-sensitive."""
        # Had issues with r+ and w+
        with open(self.file_name, 'r') as file_ref:                             # Open the file in read mode
            raw_content = file_ref.read()                                       # Store content as single string
            updated_content = raw_content.replace(target, replacement)          # Replace occurrences of target substr.

        with open(self.file_name, 'w') as file_ref:                             # Open the file in write mode
            file_ref.write(updated_content)                                     # Write updated content to file
            
        # file_ref.close()                                                      # Close the file
        self._update_date_modified()                                            # Update the time last modified
        
        
    # def replace_substring(self, target, replacement):
    #     """Replaces (target: str) with (replacement: str) everywhere in the file."""
    #     file_ref = open(self.file_name, 'r')                                    # Open the file in read/write mode
    #     raw_content = file_ref.read()                                           # Store content as single string
    #     content = raw_content
    #     updated_content = str(content).replace(target, replacement)              # Replace occurrences of target substr.
    #
    #     file_ref.write(updated_content)                                         # Write updated content to file
    #
    #     file_ref.close()                                                        # Close the file
    #     self._update_date_modified()                                            # Update the time last modified
    
        
    @staticmethod
    def _convert_file_to_list(file_name):
        import os
        
        if ".txt" not in file_name:
            file_name = str(file_name) + ".txt"                                 # Append .txt extension (if not there)
        
        if not os.path.exists(file_name):
            print("File not found.")                                            # File wasn't found
            return None
        
        file_ref = open(file_name, 'r')                                         # Open the file in read mode
        raw_content = file_ref.read()                                           # Store content as single string
        words = raw_content.split()                                             # Separate into individual words
        
        return words                                                            # Return the list of words
        


if __name__ == '__main__':
    
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    A = File("test1", "This is a file with some text")
    B = File("test2")
    C = File("test1", "This is another file with some text")
    D = File("test2")
    
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
    C.set_owner("John Doe")
    D.set_owner("Runtao Zhu")

    print(A.get_owner())
    print(D.get_owner())

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
    D.set_content("This is a new content")
    D.add_from(A)
    D.get_date()
    
    B.add_line("Hello World!")
    B.add_line("This is a new line!")
    B.delete_line(1)
    print("After appending 2 lines and deleting line 1 from B: ", end="")
    print(B.get_content())
    
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
    print(A)
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
    
    # replaces the word "this" with the word "that" everywhere in the file.
    print("File A Before replacing \"this\" with \"that\" A: ")
    print(A.get_content())
    
    A.replace("This", "That")
    print("File A After replacing \"This\" with \"That\" A: ")
    print(A.get_content())

    # Equates to true if the file contains the word
    word = "World"
    b_has_word = B.has_word(str(word))
    print("File {} contained the word {}: {}".format(B.get_name(), word, b_has_word))

    # The content of A and B are added together and written into a new file E.
    E = A + B
    print("A + B = {}".format(E.get_content()))

    # returns true, if the number of words in A is greater than the number of words in B
    print("A > B is {}".format(A > B))
    
