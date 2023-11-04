# Snake.py

from tkinter import *
from tkinter.messagebox import *
from random import randrange, randint
from time import sleep



game_width = 500
game_height = 500
snake_item = 20
snake_x = 12
snake_y = 12
snake_color = "green"
x_nav = 0
y_nav = 0


snake_list = []
snake_size = 3


virtual_x = game_width / snake_item
virtual_y = game_height / snake_item

apples_list = []
ate_apples = 0
apple_color = "red"



# Создаём игровое поле
window = Tk()
window.title("Змейка")
window.resizable(0, 0)
window.iconbitmap("Snake.ico")
window.wm_attributes("-topmost", 1)
field = Canvas(window, width = game_width, bg = "black",
				height = game_height, bd = 0,
					highlightthickness = 0)
field.pack()



# Функция прорисовки змейки
def paint_snake(field, x, y):
	global snake_list

	snake_id = field.create_rectangle(x * snake_item, 
								y * snake_item,
								x * snake_item + snake_item,
								y * snake_item + snake_item,
								fill = snake_color)
	snake_list.append([x, y, snake_id])

paint_snake(field, snake_x, snake_y)



# Прорисовка яблок
def create_apples(apples_amount):
	for i in range(apples_amount):
	
		x = randrange(virtual_x)
		y = randrange(virtual_y)
	
		apple_id = field.create_oval(x * snake_item, 
								y * snake_item,
								x * snake_item + snake_item,
								y * snake_item + snake_item,
								fill = apple_color)
	
		apples_list.append( [x, y, apple_id] )

create_apples(3)



# Функция съедания яблок
def eat_apple():
	global snake_size
	global apples_list
	global ate_apples

	for i in range( len(apples_list) ):

		if apples_list[i][0] == snake_x and apples_list[i][1] == snake_y:
			snake_size += 1
			ate_apples += 1
			field.delete( apples_list[i][2] )
			apples_list[i].clear()
			apples_list[i].clear()
			apples_list[i].insert(0, 1000)
			apples_list[i].insert(1, 1000)

			
			if ate_apples >= 3:
				create_apples( randint(1, 2) )



# Функция удаления хвоста змеи
def delete_item():
	if len(snake_list) >= snake_size:
		temp_item = snake_list.pop(0)
		field.delete( temp_item[2] )


# Функция управления змейкой
def snake_control(event):

	global snake_x
	global snake_y
	global x_nav
	global y_nav

	if event.keysym == "Up":
		x_nav = 0
		y_nav = -1
		delete_item()

	elif event.keysym == "Down":
		x_nav = 0
		y_nav = 1
		delete_item()

	elif event.keysym == "Left":
		x_nav = -1
		y_nav = 0
		delete_item()

	elif event.keysym == "Right":
		x_nav = 1
		y_nav = 0
		delete_item()

	snake_x = snake_x + x_nav
	snake_y = snake_y + y_nav
	paint_snake(field, snake_x, snake_y)

	eat_apple()


field.bind_all("<KeyPress-Up>", snake_control)
field.bind_all("<KeyPress-Down>", snake_control)
field.bind_all("<KeyPress-Left>", snake_control)
field.bind_all("<KeyPress-Right>", snake_control)



# Функция Game Over
def game_over():
	new_window = Toplevel(window)
	new_window.title("Game over")
	new_window.geometry("350x150")
	new_window.wm_attributes("-topmost", 1)
	new_window["bg"] = "black"
	new_window.resizable(0, 0)
	new_window.iconbitmap("Snake.ico")


	itog = f"Вы съели {ate_apples} яблок"

	text = Label(new_window, text = itog,
					font = "Ubuntu, 23",
					bg = "black", fg = "white")

	text.pack(side = TOP, fill = X, expand = True)


	btn_ok = Button(new_window, text = "ОК",
					font = "Ubuntu, 20",
					fg = "white", bg = "black", bd = 0,
					relief = "flat", cursor = "hand2",
					activebackground = "black",
                    activeforeground = "white",
                    command = exit)
	btn_ok.pack(side = BOTTOM, fill = X, expand = True)

	# Затемнение кнопки при наведении на неё мыши
	def have_mouse(e):
		btn_ok["fg"] = "gray"

	def not_mouse(e):
		btn_ok["fg"] = "white"

	btn_ok.bind("<Enter>", have_mouse)
	btn_ok.bind("<Leave>", not_mouse)



# Столкновение с границами
def check_borders():
	global snake_x, snake_y

	if snake_x > virtual_x or snake_x < 0:
		game_over()
		breakpoint()
		exit(1)


	elif snake_y > virtual_y or snake_y < 0:
		game_over()
		breakpoint()
		exit(1)



# Касание самого себя
def check_himself(f_x, f_y):
	if not(x_nav == 0 and y_nav == 0):
		for i in range( len(snake_list) ):
			if snake_list[i][0] == f_x and snake_list[i][1] == f_y:
				game_over()
				breakpoint()
				exit(1)



# Змейка ползает сама
while True:
	snake_x = snake_x + x_nav
	snake_y = snake_y + y_nav
	paint_snake(field, snake_x, snake_y)	
	
	delete_item()
	eat_apple()
	check_borders()	
	check_himself(snake_x + x_nav, snake_y + y_nav)
	
	window.update_idletasks()
	window.update()
	
	sleep(0.1)























window.mainloop()




