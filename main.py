from turtle import *
from spaceship import Spaceship
from enemies import Enemies, enemy_list
from bullets import Bullets
from scoreboard import ScoreBoard
from data import level
run = False

LEVEL = 1

speed = 12

window = Screen()

texts = Turtle()
texts.penup()
texts.hideturtle()
texts.color('white')
texts.goto(-100, 0)


window.bgpic('images/bg.gif')
window.tracer(0)
window.setup(width=800, height=680)
window.title("Space invaders")
window.listen()
texts.write("Press space to start", font=("Arial", 18, "normal"))

texts.goto(-170, -50)
texts.write('Press a and d to move and space to shoot', font=("Arial", 14, "normal"))
window.register_shape('images/spaceship (1).gif')
window.register_shape('images/Asset-1.gif')


spaceship = Spaceship((0, -280))
spaceship.shape('images/spaceship (1).gif')
enemies = Enemies(level=level)
scoreboard = ScoreBoard()
bullets = Bullets((spaceship.xcor(), spaceship.ycor()))


def start_game():
    global run
    texts.clear()
    run = True


def restart_game():
    global run, spaceship, scoreboard, enemies, bullets, LEVEL
    LEVEL += 1
    window.clear()
    texts.clear()
    spaceship.clear()
    scoreboard.clear()
    for i in enemy_list:
        i.clear()
    bullets.clear()
    window.tracer(0)
    window.listen()
    window.bgpic('images/bg.gif')
    spaceship = Spaceship((0, -280))
    spaceship.shape('images/spaceship (1).gif')
    enemies = Enemies(level=level)
    scoreboard = ScoreBoard()
    texts.goto(-300, 300)
    texts.write(f"Level:{LEVEL}", font=("Arial", 14, "normal"))
    bullets = Bullets((spaceship.xcor(), spaceship.ycor()))
    run = True
    game()


window.onkey(start_game, 'space')


def game():
    global run
    if run:
        window.update()
        bullets.setx(spaceship.xcor())
        bullets.forward(25)
        window.onkeypress(spaceship.go_left, "a")
        window.onkeypress(spaceship.go_right, "d")
        window.onkeypress(bullets.shoot, 'space')
        spaceship.check()
        scoreboard.update_scoreboard()
        window.update()


        for enemy in enemy_list:
            enemy.forward(speed)
            if enemy.distance(spaceship) < 20 or enemy.ycor() < -320:
                texts.goto(-40, 0)
                texts.write("Game over", font=("Arial", 18, "normal"))
                run = False
            if enemy.xcor() >= 300:
                enemy.sety(enemy.ycor() - 10)
                for _ in enemy_list:
                    enemy.setheading(180)
            if enemy.xcor() <= -300:
                enemy.sety(enemy.ycor() - 20)
                for _ in enemy_list:
                    enemy.setheading(0)

            if bullets.distance(enemy) < 18:
                enemy.hideturtle()
                enemy_list.remove(enemy)
                scoreboard.increase_score()

            if enemy_list == []:
                run = False
                texts.goto(-170, 0)
                texts.write("You win, press x to play again", font=("Arial", 18, "normal"))

    window.onkey(restart_game, 'x')

    window.ontimer(game, 20)


game()

window.exitonclick()

