import re
regex = re.compile('(?si)(?:(href|src)="([^"]*)")')
old_file = ''.join([row for row in open('C:\\Users\\jjasi\\Desktop\\budrun\\frontend\\dist\\index.html', mode='r')])
new_file = regex.sub(r'\1="/static\2"', old_file)
with open('C:\\Users\\jjasi\\Desktop\\budrun\\frontend\\dist\\index.html', 'w') as file:
    file.write(new_file)
