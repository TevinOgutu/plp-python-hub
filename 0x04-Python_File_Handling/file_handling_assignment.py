try:
   # 1. File Creation
   with open("my_file.txt", "w") as file:
       file.write("This is the first line.\n")
       file.write("Second line with a number: 42\n")
       file.write("Third line: Hello, World!\n")

   # 2. File Reading and Display
   with open("my_file.txt", "r") as file:
       content = file.read()
       print("File Contents:")
       print(content)

   # 3. File Appending
   with open("my_file.txt", "a") as file:
       file.write("Fourth line appended.\n")
       file.write("Fifth line appended with a number: 3.14\n")
       file.write("Sixth line appended.\n")

   print("File appending successful.")

except FileNotFoundError:
   print("Error: File not found.")
except PermissionError:
   print("Error: Permission denied.")
except Exception as e:
   print("Error:", str(e))

finally:
   print("File handling operations completed.")
