# Author: Jamal Huraibi, fh1328
# Assignment 4
# Question 1


# TODO: Determine how to reference file data
# e.g. Load/Read file each time or keep local copy in a str var?
# Also: Change self.file_ref to a method-only scope?
class File():
    def __init__(self, initial_file_name, initial_content=" "):
        self.file_number = None
        self.file_name = initial_file_name
        self.file_owner = " "
        self.time_modified = None
        self.content = initial_content
        self.date_modified = " "
        self.__update_file_counter()
        self.__set_date()
        
        self.file_ref = None    # TODO: Update according to future method of handling file opening
    
    
    @staticmethod
    def __update_file_counter():
        """Updates the file-number counter."""
    
    
    def get_number(self):
        """Returns the file number."""
        return self.file_number
        
        
    def get_name(self):
        """Returns the file name."""
        return self.file_name
    
    
    def set_owner(self, owner_name):
        """Updates the name of the file owner."""
        self.file_owner = owner_name
        
        
    def get_owner(self):
        """Returns the name of the file owner (if one was set). Otherwise, returns an alert that none was set."""
        if self.file_owner == " ":
            return "[No Owner Has Been Set]"                                    # Handle file having no owner
        else:
            return self.file_owner                                              # If has owner, return the name
        
        
    def __set_date(self):
        """Updates the last date and time file was modified."""
        pass
        
        
    def get_date(self):
        """Returns the last date and time file was modified."""
        return self.date_modified
        
        
    def add_line(self, text_to_add):
        """Adds a new line to the end of file."""
        self.file_ref = open(self.file_name, 'a')                               # Open the file in append mode
        
        self.file_ref.write(text_to_add)                                        # Append the new data
        self.file_ref.close()                                                   # Close the file
        
        
    def delete_line(self, line_number):
        """Deletes a specific line from file."""
        self.file_ref = open(self.file_name, 'rw')                              # Open the file in read/write mode
        
        content = self.file.read()                                              # Store file contents as single string
        content_by_lines = content.split('\n')                                  # Delimit by new line
        content_by_lines[line_number] = ""                                      # Erase content at provided line number
        
        self.file_ref.write(content_by_lines)                                   # Write the updated content
        
        self.file.close()                                                       # Close the file
        
    
    # TODO: Clarify if printing or just return raw content
    def get_content(self):
        """Fetches the entire content of the file and returns it."""
        self.file_ref = open(self.file_name, 'r')                               # Open the file in read mode
        content = self.file_ref.read()                                          # Read-in data as single string
        
        print("File Content: \n{}".format(self.file_ref))                       # Print header followed by file content
        
        
    def set_content(self, string):
        """Changes the content of the text file, overwriting any existing text."""
        pass
        
        
    def has_word(self, word_to_find):
        """Checks if the file has a specific word in it. Returns true if the word is found, otherwise returns false."""
        self.__update_local_content()
        return word_to_find in self.content
    
    
    def __update_local_content(self):
        self.file = open(self.file_name, 'r')                                   # Open the file in read mode
        self.content = self.file.read()                                         # Store file contents as single string
        self.file.close()                                                       # Close the file
        #return [boolean if file read was successful]
    
    
    # TODO: Make sure other file content is str (check: .write() cannot do numbers, p. 119)
    def add_from(self, other_file):
        """Adds the content of the other file to the end of the current file."""
        self.file_ref = open(self.file_name, 'a')                               # Open the file in append mode
        other_file_ref = open(other_file, 'r')                                  # Open the other file in read mode
        other_file_content = other_file_ref.read()                              # Record other file contents as string
        
        self.file_ref.write(other_file_content)                                 # Append the data from other file
        self.file_ref.close()                                                   # Close the file
    
    
    # TODO: Make sure unwanted items are not being counted
    def count_words(self):
        """Counts the number of words in a file and returns it."""
        self.file_ref = open(self.file_name, 'a')                               # Open the file in append mode
        raw_content = self.file_ref.read()                                      # Store content as single string
        words = raw_content.split()                                             # Separate into individual words
        
        return len(words)                                                       # len will num of indiv. words
    
    
    def replace(self, target, replacement):
        """Replaces (target: str) with (replacement: str) everywhere in the file."""
        self.file_ref = open(self.file_name, 'rw')                               # Open the file in read/write mode
        raw_content = self.file_ref.read()                                      # Store content as single string
        
        updated_content = raw_content.replace(target, replacement)              # Replace occurences of target substring
        
        self.file_ref.write(updated_content)                                    # Write updated content to file
    
    
    def open_file(self):
        self.file_ref = open(self.file_name, 'r')                               # Open the file in read mode
    
    
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
    A = File()
    B = File()
    C = File()

    print("A File Number: %" % A.getNumber())
    print("B File Number: %" % B.getNumber())
    print("C File Number: %" % C.getNumber())