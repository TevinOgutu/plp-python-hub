<center><h2>Python (Files I/O)</h2></center>
<h3>Understanding how to read and write files:</h3>

In Python, reading from and writing to files can be accomplished using the open function. The open function takes two arguments: the name of the file and the mode in which the file should be opened.

There are four modes in which a file can be opened in Python:

"r" (Read Only): This mode is used to only read the contents of a file. If the file does not exist, a FileNotFoundError will be raised.
"w" (Write Only): This mode is used to write to a file. If the file already exists, its contents will be truncated (i.e., deleted), and a new file with the same name will be created. If the file does not exist, a new file with the specified name will be created.
"a" (Append Only): This mode is used to append to an existing file. If the file does not exist, a new file with the specified name will be created.
"x" (Write Only, Exclusive Creation): This mode is used to write to a file only if the file does not already exist. If the file already exists, a FileExistsError will be raised.
