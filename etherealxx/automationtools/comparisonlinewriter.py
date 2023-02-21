import os

curdir = os.path.realpath(__file__)
maindir = os.path.abspath(os.path.join(curdir, "../../"))
mdpath = os.path.join(maindir, "ModelComparison.md")

title = input("Enter title: ")
link = input("Enter link: ")
filename = input("Enter filename: ")

# Open the markdown file for reading
with open(mdpath, "r") as file:
    lines = file.readlines()

# Find the line that contains "## Model Comparison (NSFW)"
for index, line in enumerate(lines):
    if "## Model Comparison (NSFW)" in line:
        # Add a newline above the line
        lines.insert(index+0, "")
        # Add the title below the new line
        lines.insert(index+1, f"### {title}\n\n")
        # Add another newline below the title
        # Add the image links below the new line
        lines.insert(index+2, f"{link}\n")
        lines.insert(index+3, "\n")
        lines.insert(index+4, f'<img src="modelexamples/{filename}%20seed%201.png" alt="" width="300"/><img src="modelexamples/{filename}%20seed%202.png" alt="" width="300"/><img src="modelexamples/{filename}%20seed%203.png" alt="" width="300"/>\n')
        lines.insert(index+5, "\n")
        break

# Open the markdown file for writing
print()
print("Writing lines: ")
print()
with open(mdpath, "w") as file:
    file.writelines(lines)
    
print(f"### {title}")
print(f"{link}")
print(f'<img src="modelexamples/{filename}%20seed%201.png" alt="" width="300"/><img src="modelexamples/{filename}%20seed%202.png" alt="" width="300"/><img src="modelexamples/{filename}%20seed%203.png" alt="" width="300"/>')

# Print the link
print()
print("done")
