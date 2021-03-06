# Implementation of classic arcade game Pong
# Sheena Yu
# http://www.codeskulptor.org/#user43_w0ogQPuYti_4.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = paddle2_pos = float(HEIGHT / 2)
paddle1_vel = paddle2_vel = 0.0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    hori_vel = random.randrange(2, 4)
    verti_vel = random.randrange(1, 3)
    ball_vel = [hori_vel, - verti_vel]
    if direction == LEFT:
        ball_vel[0] = - ball_vel[0] 

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = score2 = 0
    # Randomnize the direction of the spawn ball
    randNum = random.randrange(1, 3)
    if randNum == 1:
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and bounce off of the top and bottom walls
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # determine whether paddle and ball collide 
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        # if strikes left paddle
        if ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            # increase velocity of the ball by 10%
            ball_vel[0] += ball_vel[0] * 0.1
            ball_vel[1] += ball_vel[1] * 0.1            
        # if hits left side wall
        else:
            score2 += 1
            spawn_ball(RIGHT)
            
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        # if strikes right paddle
        if ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
            # increase velocity of the ball by 10%
            ball_vel[0] += ball_vel[0] * 0.1
            ball_vel[1] += ball_vel[1] * 0.1       
        # if hits right side wall
        else:
            score1 += 1
            spawn_ball(LEFT)
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    padpos1_checkvalue = paddle1_pos + paddle1_vel
    if padpos1_checkvalue <= HEIGHT - HALF_PAD_HEIGHT and padpos1_checkvalue >= HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    
    padpos2_checkvalue = paddle2_pos + paddle2_vel
    if padpos2_checkvalue <= HEIGHT - HALF_PAD_HEIGHT and padpos2_checkvalue >= HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel

    # draw paddles
    # pad1 (left)
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], 
                     [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],
                     PAD_WIDTH, 'White')
    # pad2 (right)
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], 
                     [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], 
                     PAD_WIDTH, 'White')       
    
    # draw scores
    canvas.draw_text(str(score1), [150,100], 45, "Yellow")
    canvas.draw_text(str(score2), [450,100], 45, "Yellow")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 3
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
        
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()



