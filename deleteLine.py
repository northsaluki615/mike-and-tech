import os
path_of_the_directory= './mike-and-tech-md/'



for filename in os.listdir(path_of_the_directory):
    try:
        with open(f, 'r') as fr:
            lines = fr.readlines()
    
            with open(f, 'w') as fw:
                for line in lines:
                
                    # find() returns -1
                    # if no match found
                    if line.find('date_updated') == -1:
                        fw.write(line)
        print("Deleted")
    except:
        print("Oops! something error")