import file1

print(f"File2 __name__ = {__name__}")

if __name__ == "__main__":
    print("file2 is being run directly")
else:
    print("File2 is being imported")
