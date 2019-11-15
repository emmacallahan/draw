from turtle import *
color('red',"yellow")
begin_fill()
for i in range(5):
    forward(200)
    left(216)
end_fill()

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
