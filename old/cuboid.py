# A = lb+ bh + hl
# V = lbh
# l b h
length=int(input("give the length of cuboid"))
breadth=int(input("give the breadth of cuboid"))
height=int(input("give the height of cuboid"))
area=length*breadth+breadth*height+height*length
volume=length*breadth*height
print("area of cuboid",area)
print("volume of cuboid",volume)