import requests
import time
import random
import click
from sense_hat import SenseHat
sense = SenseHat()


# Replace with your own function in Part 1
def get_direction():
 d_long = 0
 d_la = 0
 send_vel = False
   # c = click.getchar()
    #if c == '\x1b[D' or c =='a':
 while True:
  for event in sense.stick.get_events():
   
    if event.direction == "left":
        print(event.direction, event.action)   
 #   click.echo('Left')
        send_vel = True
        d_long = -1
        d_la = 0
 #   elif c == '\x1b[C' or c == "d":
 #       click.echo('Right')
    elif event.direction == "right":
        print(event.direction, event.action)
        send_vel = True
        d_long = 1
        d_la = 0
  #  elif c == '\x1b[A' or c =='w':
  #      click.echo('Up')
    elif event.direction == "up":
        print(event.direction, event.action)
        send_vel = True
        d_long = 0
        d_la = 1
  #  elif c == '\x1b[B' or c == 's':
  #      click.echo('Down')
    elif event.direction == "down":
        print(event.direction, event.action)
        send_vel = True
        d_long = 0
        d_la = -1
    else:
        d_long = 0
        d_la = 0
        print(event.direction, event.action)
       # click.echo('Invalid input :(')
        send_vel = False
    return d_long, d_la, send_vel
    

if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"
    while True:
        d_long, d_la, send_vel = get_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)
