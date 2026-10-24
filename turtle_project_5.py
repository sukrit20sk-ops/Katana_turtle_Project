import turtle
import time

# ==========================================
# SYSTEM SETUP & CANVAS
# ==========================================
screen = turtle.Screen()
screen.setup(width=1100, height=500)
screen.bgcolor("#111116")  # Premium deep charcoal canvas
screen.title("Masterwork Katana - Hand-Drawn Animation")

t = turtle.Turtle()
t.hideturtle()  # Keep the arrow invisible for a cleaner drawing look

# 💡 ANIMATION SPEEDS:
# 1 is slowest, 10 is fast. We use 3 to 6 here so it builds smoothly 
# without taking forever, while still letting you see every detail.
t.speed(4) 

def draw_polygon_slowly(points, fill_color, border_color=None, border_width=1):
    """Draws a shape step-by-step so the user can watch it form."""
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.color(border_color if border_color else fill_color, fill_color)
    t.pensize(border_width)
    t.begin_fill()
    for pt in points[1:]:
        t.goto(pt)
    t.goto(points[0])
    t.end_fill()

# ==========================================
# 1. THE HANDLE (Tsuka) & WRAPPING (Ito)
# ==========================================
# Base White Rayskin
tsuka_points = [(-97, 16), (-260, 8), (-260, -18), (-97, -16)]
draw_polygon_slowly(tsuka_points, "#f5f5f7", "#d1d1d6")
time.sleep(0.2)

# Drawing the traditional diamond wrap step-by-step
num_diamonds = 8
tsuka_width = 163  
step = tsuka_width / num_diamonds

for i in range(num_diamonds):
    x_start = -97 - (i * step)
    x_end = x_start - step
    
    y_top_start = 16 - (i * 8 / num_diamonds)
    y_top_end = 16 - ((i + 1) * 8 / num_diamonds)
    y_bot_start = -16 + (i * 2 / num_diamonds)
    y_bot_end = -16 + ((i + 1) * 2 / num_diamonds)
    y_mid_start = (y_top_start + y_bot_start) / 2
    
    # Draw interlocking structural wrap folds piece by piece
    draw_polygon_slowly([(x_start, y_top_start), (x_end, y_top_end), (x_start, y_mid_start)], "#16171a", "#090a0c")
    draw_polygon_slowly([(x_start, y_bot_start), (x_end, y_bot_end), (x_start, y_mid_start)], "#232529", "#090a0c")
    draw_polygon_slowly([(x_end, y_top_end), (x_end, y_bot_end), (x_start, y_mid_start)], "#1b1c20", "#090a0c")

# Solid gold Pommel Cap (Kashira) at the very back
kashira_points = [(-260, 8), (-270, 6), (-272, 2), (-272, -12), (-270, -16), (-260, -18)]
draw_polygon_slowly(kashira_points, "#cca43b", "#917024", border_width=2)
time.sleep(0.3)

# ==========================================
# 2. THE HANDGUARD (Tsuba)
# ==========================================
# The iron hand guard acts as the centerpiece divider
tsuba_points = [(-75, 38), (-80, 42), (-92, 42), (-97, 38), (-97, -38), (-92, -42), (-80, -42), (-75, -38)]
draw_polygon_slowly(tsuba_points, "#1e1f22", "#0d0e10", border_width=2)

# Gold spacer accents on the guard
draw_polygon_slowly([(-75, 20), (-79, 22), (-79, -22), (-75, -20)], "#cca43b")
draw_polygon_slowly([(-97, 20), (-93, 22), (-93, -22), (-97, -20)], "#cca43b")
time.sleep(0.3)

# ==========================================
# 3. THE BLADE COLLAR (Habaki)
# ==========================================
# Golden collar right before the steel begins
habaki_back = [(-50, 13), (-75, 11), (-75, -13), (-50, -12)]
draw_polygon_slowly(habaki_back, "#c49a37", "#917024")
habaki_front = [(-50, 13), (-55, 13), (-55, -12), (-50, -12)]
draw_polygon_slowly(habaki_front, "#e6c265", "#c49a37")

# ==========================================
# 4. THE BLADE STEEL (Ji & Ha)
# ==========================================
# Watch the spine forge forward smoothly
blade_spine = [(-50, 12), (180, 22), (230, 28), (245, 34), (250, 38)]
blade_edge = [(240, 20), (225, 14), (180, 7), (-50, -3)]
ji_points = [(-50, 12)] + blade_spine + [(240, 20)] + blade_edge[::-1]
draw_polygon_slowly(ji_points, "#78828c", "#505860")

# Watch the polished edge lay over the top
ha_points = [(-50, 3), (180, 7), (225, 14), (240, 20), (250, 38), (246, 22), (235, 10), (180, -2), (-50, -11)]
draw_polygon_slowly(ha_points, "#dcdfe5", "#aeb4c1")

# ==========================================
# 5. FINE DETAILING LINES
# ==========================================
# Drawing the Blood Groove (Bo-Hi) down the length
t.penup()
t.pensize(2)
t.color("#3a3f44")
t.goto(-40, 7)
t.pendown()
t.goto(175, 16)
t.goto(215, 21)

# Slowly etching the wavy tempering line (Hamon)
t.penup()
t.pensize(1.5)
t.color("#f0f2f5")
t.goto(-50, -3)
t.pendown()
hamon_waves = [
    (-20, -2), (10, -5), (40, 0), (70, -4), 
    (100, 2), (130, -2), (160, 4), (190, 1), 
    (220, 8), (235, 12), (246, 22)
]
for wp in hamon_waves:
    t.goto(wp)

screen.mainloop()
