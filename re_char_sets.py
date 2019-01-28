import re

# \w - Matches single alpha numeric characters [a-zA-Z0-9_]
# \W is opposite of \w
print re.search('\w\w\w', "gopi valleru").group()
print re.search('\w\w\w', "go-pi_valleru").group()
print re.search('\w\w\W', "go-pi_valleru").group()

# quantifiers
# + = 1 or more
# ? = 0 or 1
# * = 0 or more
# {n,m} = n to m repetitions. Ex: {1,3}, {,3}, {3,}

# 1-255 = 1-9, 10-99, 100-199, 200-250, 250-255
# (([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).{3})([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])

ipv4_expr = '(([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
print re.search(ipv4_expr, r'208.93.27.50').group()

# \d - Matches any single digit [0-9]
# \D - Opposite to \d
# \s - May whitespace char. i.e newline, spaces, tabs.
# \S - Opposite to \s
print re.search('\S+', 'go-pi_valleru+# in').group()
# . - Any char. except new line
print re.search('.+', "gopi valleru\nin usa").group()
# - is a meta char when used in [] (custom char set)
print re.search('[a-z]', 'gopi valleru').group()
