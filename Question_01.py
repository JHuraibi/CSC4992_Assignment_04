# Author: Jamal Huraibi, fh1328
# Assignment 4
# Question 1


class File():
    def __init__(self, initial_file_name, initial_content=" "):
        self.fileNumber = None
        self.fileName = initial_file_name
        self.fileOwner = " "
        self.timeModified = None
        self.content = initial_content
        self.__update_file_counter()
        self.set_date()
    
    
    @staticmethod
    def __update_file_counter():
        """Updates the file-number counter"""
    
    
    def get_number(self):
        """Returns the file number"""
        return self.fileNumber
        
        
    def get_name(self):
        """Returns the file name."""
        return self.fileName
    
    
    def set_owner(self, owner_name):
        """Adds the name of the file owner."""
        self.fileOwner = owner_name
        
        
    def get_owner(self):
        """Returns the name of the file owner (if one was set). Otherwise, returns an alert that none was set."""
        if self.fileOwner == " ":
            return "[No Owner Has Been Set]"
        else:
            return self.fileOwner
        
        
    def set_date(self):
        """Adds the last date and time file was modified."""
        
        
    def get_date(self):
        """Returns the last date and time file was modified."""
        
        
    def add_line(self, text_to_add):
        """Adds a new line to the end of file."""
        
        
    def delete_line(self, line_number):
        """Deletes a specific line from file."""
        
        
    def get_content(self):
        """Fetches the entire content of the file and returns it."""
        
        
    def set_content(self, string):
        """Changes the content of the text file, overwriting any existing text."""
        
        
    def has_word(self):
        """Checks if the file has a specific word in it. Returns true if the word is found, otherwise returns false."""
    
    
    def add_from(self):
        """Adds the content of the other file to the end of the current file."""
    
    
    def count_words(self):
        """Counts the number of words in a file and returns it."""
    
    
    def replace(self, target, replacement):
        """Replaces (target: str) with (replacement: str) everywhere in the file."""
        
    
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