import cgi
import json
import color-names.json

form = cgi.FieldStorage()

with open("color-names.json", "r") as read_file:
    data = json.load(read_file)

# get an input filed from the form called 'name'
# and assign it's value to a local variable called v_name
to_be_checked_color = form.getvalue('color')

if to_be_checked_color.title() in data.value():
    response = "Nice"
else:
    response = "Ohh!"

# send an html response.
print("""
<html>
<body>
<p>
%s
</p>
</body>
</html>
""" % response)
