import os

folder = "./test_files"
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        new_name = "renamed_" + filename
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

print("Files renamed successfully!")
