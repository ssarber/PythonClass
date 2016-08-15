#!/usr/bin/python
print('Content-type: text/html\n')

import circle
from htmllib import content_type, template

i2 = 0
c1 = circle.Circle(0, 0, 20)
c2 = circle.Circle(0, 0, 20)
for i in range(20):
    print('--')
    # print('Circle 1: ',c1)
    # print('Circle 2: ',c2)
    print("Collision? ",circle.Circle.is_collision(c1, c2))
  
    i2 += i
    c1.move(i, i)
    c2.move(i, i2)

some_input = "some input from a form (not to be trusted!)"
content_type()
template(title='This is My Beautiful Web Page',content=(some_input))


#!/usr/bin/python
print('Content-type: text/html\n')
print("<head><title>Lab4.1 - Circles</title>");
print("<h3>lab4.1.py</h3>");

import circle
from htmllib import content_type, template

i2 = 0
c1 = circle.Circle(100, 0, 20)
c2 = circle.Circle(200, 0, 20)

print("<pre>" + "Circle 1: This is a circle located at %d, %d and has a radius of %d" %(c1.x, c1.y, c1.radius) + "</pre>")
print("<pre>" + "Circle 2: This is a circle located at %d, %d and has a radius of %d" %(c2.x, c2.y, c2.radius) + "</pre>")
distance_between_radii = c1.radius + c2.radius
print("<pre>" + "Minimum distance between their radii: %d" %distance_between_radii + "</pre>")

print("""<style type="text/css"> body {background-color:E6E8FA;}tr.warning 
{background-color:tomato}#collisions-table {font-size:1.5em;border:solid 1px gray;
border-collapse:collapse}#collisions-table td, #collisions-table th {border:solid 1px #ccc;padding:6px 8px;}
div#collisions{overflow:auto;width:900px;margin:2em auto}.circle1 {text-align:center;font-size:24px;position:absolute;
background:url(circle1small.png);width:40px;height:40px}.circle2 
{text-align:center;font-size:24px;position:absolute;background:url(circle2small.png);width:40px;height:40px}.True 
{color:black} .None {color:blue}</style>""")
print("</head>")
print("<body>")
print('<table border="1"')
print('<tr><th>#</th><th colspan=2>Circle One<div style="width:45%;float:left">x</div><div style="width:45%;float:right">y</div></th><th colspan=2>Circle Two<div style="width:45%;float:left">x</div><div style="width:45%;float:right">y</div></th><th>Distance</th><th>Collision?</th></tr>')
for i in range(10):
    collision = circle.Circle.is_collision(c1, c2)
    if collision: 
        print("<tr class=warning>")
        print("<td>" + "%d" %i + "</td>")
        print("<td>" + "%d" %c1.x + "</td>")
        print("<td>" + "%d" %c1.y + "</td>")
        print("<td>" + "%d" %c2.x + "</td>")
        print("<td>" + "%d" %c2.y + "</td>")
        print("<td>" + "%d" % circle.Circle.distance(c1, c2) + "</td>")
    
        print("<td>" + "%s" % circle.Circle.is_collision(c1, c2) + "</td>")
        print("</tr>") 
    else
        print("<tr>")
        print("<td>" + "%d" %i + "</td>")
        print("<td>" + "%d" %c1.x + "</td>")
        print("<td>" + "%d" %c1.y + "</td>")
        print("<td>" + "%d" %c2.x + "</td>")
        print("<td>" + "%d" %c2.y + "</td>")
        print("<td>" + "%d" % circle.Circle.distance(c1, c2) + "</td>")
    
        print("<td>" + "%s" % circle.Circle.is_collision(c1, c2) + "</td>")
        print("</tr>") 
        
    i2 += i
    c1.move(i, i)
    c2.move(i, i2)
#     print("<td>" + "%d" %c1.x + "</td>")

print("<style>body {background:url(data:image/gif;base64,%d)}</style>", %file)
print("</table>")

#   print('Circle 2: ',c2)
#     print("Collision? ",circle.Circle.is_collision(c1, c2))
#   
#     i2 += i
#     c1.move(i, i)
#     c2.move(i, i2)
# 
# some_input = "some input from a form (not to be thusted!)"
# content_type()
# template(title='This is My Beautiful Web Page',content=(some_input))

