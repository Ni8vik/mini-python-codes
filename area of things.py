# area of shapes
class area():
    def square(hight, width):
        asquare= hight * width
        print(f"the area of square is {asquare}")

    def triangle(hight, width):
        ariangle=.5*width*hight
        print(f"the area of triangle is {ariangle}")
    
    def circle(radius):
        pi=3.14
        aircle= pi*radius*radius
        print(f"the area of circle is {aircle}")


lopp=1
while lopp==1:

    x= input("what your desired shape(square, triangle, circle)")  

    if x=="circle":
        radi=int(input("whats the radius of the circle"))
        print(area.circle(radi))
    elif x=="triangle":
        higt =int(input("whats the height of the triangle"))
        widt =int(input("whats the width of the triangle"))
        print(area.triangle(higt,widt))
    elif x=="square":
        width=int(input("whats the width of the square"))
        hight=int(input("whats the height of the square"))
        print(area.square(hight, width))
    elif x=="exit":
        lopp=0
    else:
        print("sorry we dont have that shape")
    

    

