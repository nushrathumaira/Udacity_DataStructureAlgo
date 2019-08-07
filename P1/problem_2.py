import os
fileList = []
def find_files(suffix,path):
    """
    Find all files beneath path with file name suffix

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
      a list of paths
    """
    #fileList = []
    if not os.path.isdir(path):
        return None

    for file in os.listdir(path):
            if os.path.isfile(os.path.join(path,file)):
                #print("is a file\n")
                if file.endswith(suffix):
                    #print("ends with suffix\n")
                    fileList.append(os.path.join(path,file))
            elif os.path.isdir(os.path.join(path,file)):
                 #print("is a dir\n")
                 find_files(suffix,os.path.join(path,file))
                 """
                 for f in os.listdir(os.path.join(path,file)): 
                    if file.endswith(suffix):
                        #print("ends with suffix")
                        fileList.append(os.path.join(path,file))
                 """


    return fileList

# test cases
files = find_files(".c","./testdir/")
for f in files:
    print(f)
print(".....................")
files = find_files(".h","./testdir")
for f in files:
    print(f)
print(".....................")
files = find_files(".z", "./testdir")
print(".....................")

# outputs
"""
./testdir/subdir1/a.c
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir5/a.c
./testdir/t1.c
.....................
./testdir/subdir1/a.c
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir5/a.c
./testdir/t1.c
./testdir/subdir1/a.h
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir5/a.h
./testdir/t1.h
.....................
.....................
"""
