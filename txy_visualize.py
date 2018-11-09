#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.animation as animation

infile="waveeq_out"

with open(infile, 'r') as f:
    data = [[float(i) for i in line.split()] for line in f.readlines()]

rangex=[min(line[1] for line in data), max(line[1] for line in data)]
print(rangex)
yrange=[min(line[2] for line in data), max(line[2] for line in data)]
print(yrange)

data_hashtable = {
    float(k): [
               [
                l[1],
                l[2]
                ]
               for l in data if l[0] == float(k)
               ]
               for k in set([l[0] for l in data])}

def get_data(time):
    x=[line[0] for line in data_hashtable[time]]
    y=[line[1] for line in data_hashtable[time]]
    return x, y

def plot_data(time):
    x, y = get_data(time)
    plt.plot(x,y)
    plt.show()

# for time in sorted(data_hashtable.keys()):
#     plot_data(time)

#yrange=(-100,100)


fig = plt.figure()
ax = plt.axes(xlim=(rangex[0],rangex[1]), ylim=(yrange[0],yrange[1]))
line, = ax.plot([], [], lw=2)
plt.setp(line, color='B', linewidth=3.0)
def init():
    line.set_data([], [])
    return line,

def animate_singlescale(i):
    t = sorted(set(data_hashtable.keys()))[i]
    x, y = get_data(t)
    line.set_data(x,y)
    return line,

animate=animate_singlescale
nframes=len(data_hashtable.keys())
interv=30
blitp=True

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=nframes, interval=interv, blit=blitp)    

# anim.save("out.mp4", fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
