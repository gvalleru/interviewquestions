import re

# search a pattern in a string
print re.search("g", "gopi")
# You get none coz you are looking for n in new line.
print re.search("n", "\n")
# You can escape special character
print re.search("n", "\\n")
# Or you can declare the string as raw string
print re.search("n", r"\n")

# \n is new line. You can convert this meta char in python regex to a raw string
print re.search(r"\n", "\n\n")
print re.search(r"\n", r"\n\n")


# search method searches anywhere but only matches first instance but works with new line
# match only looks at the beginning of the line

print re.match("go", "pi gopi")
print re.search("go", "pigo gopi").group()
print re.search("go", "pigo gopi").start()
print re.search("go", "pigo gopi").end()
print re.search("g|o", "pigo gopi")
# findall will find all instances and returns a list
print re.findall("g|o", "pigo gopi\ngopi")
