import sys
import os

def reverse_file(inputpath, outputpath):
    try:
        with open(inputpath, 'r') as infile:
            data = infile.read()
        with open(outputpath, 'w') as outfile:
            outfile.write(data[::-1]) 
        print(f"File {inputpath} has been reversed and saved to {outputpath}.")

    except Exception as e:
        print(f"Error: {e}")

def copy_file(inputpath, outputpath):
    try:
        with open(inputpath, 'r') as infile:
            data = infile.read()
        with open(outputpath, 'w') as outfile:
            outfile.write(data)
        print(f"File {inputpath} has been copied to {outputpath}.")

    except Exception as e:
        print(f"Error: {e}")

def duplicate_file(inputpath, n):
    try:
        with open(inputpath, 'r') as infile:
            data = infile.read()
        with open(inputpath, 'w') as outfile:
            outfile.write(data * int(n))
        print(f"File {inputpath} has been duplicated {n} times.")
    
    except Exception as e:
        print(f"Error: {e}")

def replace_string(inputpath, needle, newstring):
    try:
        with open(inputpath, 'r') as infile:
            data = infile.read()
        modified_data = data.replace(needle, newstring)
        with open(inputpath, 'w') as outfile:
            outfile.write(modified_data)
        print(f"String {needle} has been replaced with {newstring} in file {inputpath}.")
    
    except Exception as e:
        print(f"Error: {e}")

def validate_args(args):
    if len(args) < 3:
        print("Usage: python FileManipulator.py <command> <arguments>")
        sys.exit(1)
    command = args[1]
    if command not in ["reverse", "copy", "duplicate-contents", "replace-string"]:
        print("Invalid command. Available commands: reverse, copy, duplicate-contents, replace-string")
        sys.exit(1)

if __name__ == "__main__":
    validate_args(sys.argv)

    command = sys.argv[1]
    if command == "reverse":
        if len(sys.argv) != 4:
            print("Usage: python FileManipulator.py reverse <inputpath> <outputpath>")
        else:
            reverse_file(sys.argv[2], sys.argv[3])
    
    elif command == "copy":
        if len(sys.argv) != 4:
            print("Usage: python FileManipulator.py copy <inputpath> <outputpath>")
        else:
            copy_file(sys.argv[2], sys.argv[3])
    
    elif command == "dauplicate-contents":
        if len(sys.argv) != 4:
            print("Usage: python FileManipulator.py duplicate-contents <inputpath> <n>")
        else:
            duplicate_file(sys.argv[2], sys.argv[3])
        
    elif command == "replace-string":
        if len(sys.argv) != 5:
            print("Usage: python FileManipulator.py replace-string <inputpath> <needle> <newstring>")
        else:
            replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
    
    else:
        print("Unknown command. Available commands: reverse, copy, duplicate-contents, replace-string")
    
