#catch the turtle oyunu
import turtle
import random
import time

score = 0
time_left = 30
game_running = True

# Ekran ve turtle ayarları
screen = turtle.Screen()
screen.title("Catch the Turtle")
screen.bgcolor("lightblue")


# Skor ve süreyi güncelle
def update_score_time():
    pen.clear()
    pen.write("Skor: " + str(score) + "  Süre: " + str(time_left), align="center", font=("Arial", 16, "normal"))

# Kaplumbağaya tıklanınca
def catch_turtle(x, y):
    global score
    if game_running:
        score += 1
        update_score_time()
        move_turtle()

# Kaplumbağayı rastgele konuma taşı
def move_turtle():
    if game_running:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t.goto(x, y)

# Süreyi azalt
def countdown():
    global time_left, game_running # neden global ekledik çünkü fonksiyon içinde değiştiriyoruz değişkeni
    if time_left > 0:
        time_left -= 1
        update_score_time()
        screen.ontimer(countdown, 1000)
    else:
        game_running = False
        pen.clear()
        pen.write("Oyun Bitti! Skorun: " + str(score), align="center", font=("Arial", 18, "bold"))
        t.hideturtle()



# Kaplumbağa ayarları
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.speed(0)
t.goto(0, 0)
t.onclick(catch_turtle)

pen = turtle.Turtle()
pen.hideturtle()

pen.penup()# Kalem kaldırıldı
pen.goto(0, 260)# Skor ve süre ekranın üstünde

update_score_time()

# Kaplumbağanın sürekli kaçmasını sağla
def auto_move():
    if game_running:
        move_turtle()
        screen.ontimer(auto_move, 800)  # 0.8 saniyede bir kaçar

auto_move()
countdown()

turtle.done()