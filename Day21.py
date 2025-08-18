#########################################################TURTLE#########################################################
#########################################################Day 21#########################################################
#python.orgdan turtle dokumantasyonu incelenmeli mutlaka
'''
import turtle
drawingBoard = turtle.Screen()#bir çizim ekranı oluşturur ve bunu değişkene atar
drawingBoard.bgcolor("purple")#bg = background dan gelir arka plan rengini ayarlar
drawingBoard.title("Python Turtle")#ekran başlığını ayarlar

turtleInstance = turtle.Turtle()#turtle sınıfından bir örnek oluşturur çizimi yapacak olan nesne yani
turtleInstance.forward(100)#turtle nesnesi 100 birim ileri gider



turtleInstance2=turtle.Turtle()#turtle sınıfından ikinci bir örnek oluşturur
#turtleInstance2.left(180)
turtleInstance2.forward(100)

#square çizme for ile
turtleInstance3 = turtle.Turtle()
for i in range(4):
    turtleInstance3.forward(100)
    turtleInstance3.right(90)
turtle.done()#turtle çizimini tamamlar ve pencereyi kapatmaz bunu en sonda yazarız

#square çizme while döngüsü ile
import turtle
turtleInstance3 = turtle.Turtle()
x=0
while x<=4:
    turtleInstance3.forward(100)
    turtleInstance3.right(90)
    x+=1
'''

'''
#8gen çizme
import turtle
cizilenCizgi= turtle.Turtle()

for i in range (8):
    cizilenCizgi.forward(50)
    cizilenCizgi.right(45)
    cizilenCizgi.forward(50)
    cizilenCizgi.right(45)


#yıldız çizme
import turtle
cizgi = turtle.Screen()
cizgi.bgcolor("green")
cizgi.title("Python Turtle")
cizgi=turtle.Turtle()#oku oluşturur
for i in range(5):
    cizgi.forward(100)
    cizgi.right(144)  #Yıldızın iç açısı 144 derece

'''
# Karelerin iç içe çizilmesi
import turtle
instance=turtle.Screen()
instance.bgcolor("blue")
instance.title("Python Turtle")

cizgi=turtle.Turtle()
cizgi.color("red")

def fonk(size):
    for i in range(4):
        cizgi.forward(size)
        cizgi.right(90)
        size=size-5

fonk(150)
fonk(130)
fonk(110)
fonk(90)
fonk(80)
fonk(60)
fonk(40)
fonk(20)

turtle.done()

#başka örnek daire
import turtle
ekran=turtle.Screen()
ekran.bgcolor("black")
ekran.title("Python Turtle")
cizgi=turtle.Turtle()
cizgi.color("blue")
turtle_colors=["red", "blue", "green", "yellow", "purple", "orange"]

for i in range(15):
    cizgi.color(turtle_colors[i % 6])  # Renkleri sırayla kullanır
    cizgi.circle(10 * i)  # 50 birim yarıçaplı daire çizer
    cizgi.circle(-10 * i)
    cizgi.left(i)


turtle.done()#veya turtle.mainloop() kullanabilirsiniz #turtle.done() pencereyi kapatmaz turtle.mainloop() ise pencereyi kapatır


#kullanıcıyla etkileşimli bişeyler yapalım...
import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")
turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading()-100)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading()+100)

def clear_screen():
    turtle_instance.clear()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

def turtle_return_home():
    turtle_instance.home()

drawing_board.listen()# dinleme moduna alır nesneyi
drawing_board.onkey(key="space",fun=turtle_forward)#space tuşuna basıldığında turtle_forward fonksiyonunu çağırır () koymadık çünkü fonksiyonu reference olarak verdik çalıştırmasına gerek yok
drawing_board.onkey(key="Down",fun=rotate_angle_right)
drawing_board.onkey(key="Up",fun=rotate_angle_left)
drawing_board.onkey(key="c",fun=clear_screen)
drawing_board.onkey(key="q",fun=turtle_pen_up)
drawing_board.onkey(key="w",fun=turtle_pen_down)
drawing_board.onkey(key="h",fun=turtle_return_home)

drawing_board.exitonclick()#amacı pencereyi kapatmak için tıklamayı bekler
#turtle.done()



