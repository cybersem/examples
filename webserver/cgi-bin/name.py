#!C:/Python34

import cgi

form = cgi.FieldStorage()

print('Content-type: text/html\n')
print('<title>Result</title>')

if not 'user' in form:
    print('</br><h1>Name is empty! Try again!</h1>\n<a href="../index.html">Back</a>')
else:
    print('</br><h1>Hello, <i>%s</i>!</h1>\n<a href="../index.html">Back</a>' % cgi.escape(form['user'].value))

print('</body>')