## Reading a file
r = open ('/etc/passwd')
# same as:
# r = open ('/etc/passwd’, ‘r’)
passwd = r.readlines()
for line in passwd:
    line = line.strip()
    size = len (line)
    print (size, line)
r.close()