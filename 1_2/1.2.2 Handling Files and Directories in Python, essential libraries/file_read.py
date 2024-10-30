 #activating virtual environment
# venv\Scripts\activate
with open('file_read.txt','r') as file:
    
    # OPENING FILES AND CLOSING IT USING CONTEXT MANAGER
    
    # file.read(1) - for reading a specific chunck of a file,takes a number as arg
    
    # for basic reading,can take arg of lines to read
    
    # file.readlines() - for reding everyline of the file
    
    # file.readline() - for reding a single line of the file[in a list]
    
    # for line in file:
    #     print(f"** {line}")
    
    
    
    size_to_read = 10
    file_contents = file.read(size_to_read)
    print(file_contents)
    
    file.seek(1)
    # seek is used to move the pointer to a specific position in the file,0 for beginning
    file_contents = file.read(size_to_read)
    print(file_contents)
    
    
    
    
    # reading chuncks of a file
    # while len(file_contents) > 0:
        # print(file_contents, end="*")
        
        # this line is called to check if there is anymore chuncks to read,else the while loop will be infinite
        # file_contents = file.read(size_to_read)
    
    print(file.tell())
    # tell as the name suggests tells the position of the pointer in the file for read/write operations