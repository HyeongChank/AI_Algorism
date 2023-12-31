import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

def f(x):
    return 8*(x -10) * np.sin(0.5 * x-5)+200

def fd(x):
    # 미분
    return 4* (x-10) * np.cos(0.5*x-5) + 8* np.sin(0.5 * x-5)
x_min = -30
x_max = 30
x = np.linspace(x_min, x_max, 200)
y = f(x)
r = 0.54 # Learning Rate
x_est = 25  # 시작 지점
y_est = f(x_est)

def animate(i):
    global x_est
    global y_est
    x_est = x_est - fd(x_est) * r
    y_est = f(x_est)

    scat.set_offsets([[x_est, y_est]])
    text.set_text(f"Value : {y_est}")
    line.set_data(x,y)
    return line, scat, text

def init():
    line.set_data([],[])
    return (line,)

fig, ax = plt.subplots()
ax.set_xlim([x_min, x_max])
ax.set_ylim([-5, 500])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
(line,)  = ax.plot([],[])
scat = ax.scatter([],[], c = 'red')
text = ax.text(-25,450,"")
ani = animation.FuncAnimation(fig, animate, 30, init_func=init, interval = 100, blit = True)
plt.show()
        