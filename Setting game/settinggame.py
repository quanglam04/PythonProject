import re
import tkinter as tk
import subprocess
from tkinter import PhotoImage, Button,  Canvas,messagebox
from tkinter import ttk
import pygame
from pygame import mixer

subprocess.run(["test reso.exe"])
resolution = ""
try:
    with open('screen_resolution.txt', 'r') as f:
        resolution = f.readline().strip()
except FileNotFoundError:
    resolution = "Error"


match = re.search(r"(\d+)x(\d+)", resolution)
height, width = 0, 0
if match:
    width = int(match.group(1))
    height = int(match.group(2))
else:
    width = 1280
    height = 720
pygame.init()

resolutions = ["(800x600) 4:3", "(1024x768) 4:3", "(1128x634) 564:317", "(1280x720) 16:9",
               "(1280x1024) 5:4", "(1366x768) 683:384", "(1600x900) 16:9", "(1680x1050) 8:5",
               "(1760x990) 16:9", "(1920x1080) 16:9","(2880x1800) 8:5"]


def recommend_reso():
    tmp = "* (recommend)"
    resolution_map = {
        (800, 600): 0,
        (1024, 768): 1,
        (1128, 634): 2,
        (1280, 720): 3,
        (1280, 1024): 4,
        (1366, 768): 5,
        (1600, 900): 6,
        (1680, 1050): 7,
        (1760, 990): 8,
        (1920, 1080): 9,
        (2880,1800):10
    }
    if (width, height) in resolution_map:
        index = resolution_map[(width, height)]
        resolutions[index] += tmp

recommend_reso()


def load_setting():
    try:
        with open("Saved.txt", 'r') as f:
            lines = f.readlines()
            saved_resolution = lines[0].strip() if len(lines) > 0 else resolutions[0]
            saved_bgm = float(lines[1].strip()) if len(lines) > 1 else 50
            saved_sfx = float(lines[2].strip()) if len(lines) > 2 else 50
            saved_screen = lines[3].strip() if len(lines) > 3 else "True"
            button_states = [
                lines[4].strip() if len(lines) > 4 else "w",
                lines[5].strip() if len(lines) > 5 else "s",
                lines[6].strip() if len(lines) > 6 else "d",
                lines[7].strip() if len(lines) > 7 else "a",
                lines[8].strip()  if len(lines) > 8 else "q",
                lines[9].strip() if len(lines) > 9 else "Up",
                lines[10].strip() if len(lines) > 10 else "Down",
                lines[11].strip() if len(lines) > 11 else "Right",
                lines[12].strip() if len(lines) > 12 else "Left",
                lines[13].strip() if len(lines) > 13 else "0",
                lines[14].strip() if len(lines) > 14 else "y",
                lines[15].strip() if len(lines) > 15 else "h",
                lines[16].strip() if len(lines) > 16 else "j",
                lines[17].strip() if len(lines) > 17 else "g",
                lines[18].strip() if len(lines) > 18 else "f",
                lines[19].strip() if len(lines) > 19 else "8",
                lines[20].strip() if len(lines) > 20 else "2",
                lines[21].strip() if len(lines) > 21 else "6",
                lines[22].strip() if len(lines) > 22 else "4",
                lines[23].strip() if len(lines) > 23 else "1",
            ]

            return saved_resolution, saved_bgm, saved_sfx, saved_screen, button_states

    except FileNotFoundError:
        return resolutions[0], 50, 50, "None", button_states


def update_BGM(value):
    BGM_label.config(text=f"Back Ground Music : {int(round(float(value)))}")
def update_SFX(value):
    SFX_label.config(text=f"Sound Effects : {int(round(float(value)))}")
def on_select(value):
    selected.set(value)
    print(f"Selected option: {value}")
def save_setting():
    selected_resolution = resolution_menu.get()
    selected_bgm = BGM_change.get()
    selected_sfx = SFX_change.get()
    selected_screen = selected.get()
    arrow_map = {
        "↑": "Up",
        "↓": "Down",
        "←": "Left",
        "→": "Right",
    }
    button_states = [
        #Player 1
        arrow_map.get(Go_ahead_1.cget("text"), Go_ahead_1.cget("text")),
        arrow_map.get(Go_back_1.cget("text"), Go_back_1.cget("text")),
        arrow_map.get(Rotate_right_1.cget("text"), Rotate_right_1.cget("text")),
        arrow_map.get(Rotate_left_1.cget("text"), Rotate_left_1.cget("text")),
        arrow_map.get(Shoot_1.cget("text"),Shoot_1.cget("text")),
        # Player 2
        arrow_map.get(Go_ahead_2.cget("text"), Go_ahead_2.cget("text")),
        arrow_map.get(Go_back_2.cget("text"), Go_back_2.cget("text")),
        arrow_map.get(Rotate_right_2.cget("text"), Rotate_right_2.cget("text")),
        arrow_map.get(Rotate_left_2.cget("text"), Rotate_left_2.cget("text")),
        arrow_map.get(Shoot_2.cget("text"),Shoot_2.cget("text")),
        # Player 3
        arrow_map.get(Go_ahead_3.cget("text"), Go_ahead_3.cget("text")),
        arrow_map.get(Go_back_3.cget("text"), Go_back_3.cget("text")),
        arrow_map.get(Rotate_right_3.cget("text"), Rotate_right_3.cget("text")),
        arrow_map.get(Rotate_left_3.cget("text"), Rotate_left_3.cget("text")),
        arrow_map.get(Shoot_3.cget("text"),Shoot_3.cget("text")),
        # Player 4
        arrow_map.get(Go_ahead_4.cget("text"), Go_ahead_4.cget("text")),
        arrow_map.get(Go_back_4.cget("text"), Go_back_4.cget("text")),
        arrow_map.get(Rotate_right_4.cget("text"), Rotate_right_4.cget("text")),
        arrow_map.get(Rotate_left_4.cget("text"), Rotate_left_4.cget("text")),
        arrow_map.get(Shoot_4.cget("text"),Shoot_4.cget("text"))
    ]
    with open('Saved.txt', 'w') as f:
        f.write(f"{selected_resolution}\n")
        f.write(f"{selected_bgm}\n")
        f.write(f"{selected_sfx}\n")
        f.write(f"{selected_screen}\n")
        for state in button_states:
            f.write(f"{state}\n")
def start_game():
    subprocess.run(["main.exe"])




saved_resolution,saved_bgm,saved_sfx,saved_screen,button_states=load_setting()
def reload_key():
    key_map = {
        "Up": "↑",
        "Down": "↓",
        "Left": "←",
        "Right": "→",
    }
    for i in range(20):
        button_states[i]=key_map.get(button_states[i],button_states[i])
    return
reload_key()
print(saved_resolution)
print(saved_bgm)
print(saved_sfx)
print(saved_screen)
print(button_states)
def show_frame(frame):
    my_canvas.delete("all")
    my_canvas.create_image(0, 0, image=image_path, anchor="nw")  # Re-create the background image
    my_canvas.create_window(279, 43, window=control_frame)
    if frame==display_index_frame:
        my_canvas.create_window(399, 190, window=frame,width=395)
    else:
        my_canvas.create_window(399,192,window=frame,width=395)
    my_canvas.create_window(557, 350, window=save_but)
    my_canvas.create_window(242, 350, window=start_but)
def on_button_click():
    click=mixer.Sound("toggle.wav")
    click.set_volume(1)
    click.play()
def on_button_click_2():
    click=mixer.Sound("toggle original.wav")
    click.set_volume(1)
    click.play()

root = tk.Tk()
root.minsize(width=730, height=434)
root.resizable(width=False, height=False)


image_path = PhotoImage(file=r"GUI.png")


my_canvas = Canvas(root, width=730, height=434)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0, 0, image=image_path, anchor="nw")


control_frame = tk.Frame(my_canvas,height=10)
general_setting = tk.Button(control_frame, text="General setting",command=lambda: show_frame(display_index_frame))
general_setting.bind("<Button-1>",lambda e :on_button_click())
controller = Button(control_frame, text="Controller",command=lambda: show_frame(controller_frame))
general_setting.grid(row=0, column=0)
controller.grid(row=0, column=1)
controller.bind("<Button-1>",lambda e:on_button_click())

my_canvas.create_window(279, 43, window=control_frame)


display_index_frame = tk.Frame(my_canvas, pady=10)
resolution_frame = tk.LabelFrame(display_index_frame, width=200, height=100,pady=5 ,text="Resolution", relief="groove")
resolution_frame.pack()
resolution_menu = ttk.Combobox(resolution_frame, width=60,state="readonly")
resolution_menu['values'] = resolutions
resolution_menu.pack(pady=10)
resolution_menu.bind("<Button-1>",lambda e:on_button_click())

my_canvas.create_window(399, 190, window=display_index_frame,width=395)
resolution_menu.set(saved_resolution)
resolution_menu.pack()

sound_setting=tk.LabelFrame(display_index_frame,width=600,height=50,text="Sound",relief="groove")
sound_setting.pack()
BGM_label = tk.Label(sound_setting, text=f"Back Ground Music: {saved_bgm}", font=("Arial", 10))
BGM_label.pack(pady=5)
BGM_change=ttk.Scale(sound_setting,from_=0,to=100,orient="horizontal",command=update_BGM,length=380)
BGM_change.set(saved_bgm)
BGM_change.pack(fill="x")
SFX_label = tk.Label(sound_setting, text=f"Sound Effects: {saved_sfx}", font=("Arial", 10))
SFX_label.pack(pady=5)
SFX_change = ttk.Scale(sound_setting, from_=0, to=100, orient="horizontal", command=update_SFX, length=380)
SFX_change.set(saved_sfx)
SFX_change.pack(fill="x")

screen_mode=ttk.LabelFrame(display_index_frame,width=315,height=50,text="Screen mode")
screen_mode.pack()
selected=tk.StringVar(value=saved_screen)
window_mode=tk.Radiobutton(screen_mode,text="Window mode",variable=selected,value="True",command=lambda: on_select("True") )
full_screen=tk.Radiobutton(screen_mode,text="Full screen",variable=selected,value="False",command=lambda: on_select("False") )
window_mode.grid(row=0,column=0,padx=48)
full_screen.grid(row=0,column=1,padx=48)
window_mode.bind("<Button-1>",lambda e: on_button_click_2())
full_screen.bind("<Button-1>",lambda e:on_button_click_2())

save_but=Button(root,text="Save",command=save_setting,width=10,height=1)
save_but.pack()
save_but.bind("<Button-1>",lambda  e:on_button_click_2())
my_canvas.create_window(557,350,window=save_but)

start_but=Button(root,text="Start",command=start_game,width=10,height=1)
start_but.pack()
start_but.bind("<Button-1>",lambda  e:on_button_click_2())
my_canvas.create_window(242,350,window=start_but)

def received_but(button):
    button.focus_set()
    button.bind("<KeyPress>",lambda e: update_button_text(button,e))

def update_button_text(button,event):
    special_key={
        "Up": "↑",
        "Down": "↓",
        "Left": "←",
        "Right": "→",
        "comma": ',',
        "period": '.',
        "semicolon": ';',
        "quoteright": "'",
        "bracketleft": '[',
        "bracketright": ']',
        "backslash": '\\',
        "quoteleft": '`',
        "slash": '/',
        "asterisk": '*',
        "minus": '-',
        "plus": '+',
        "space":"Space",
        "Prior":"PgUp",
        "Next":"PgDn",
        "Return":"Enter",
    }
    key=event.keysym
    print(key)
    key=special_key.get(key,key)
    coppy_states = [
        # Player 1
        Go_ahead_1.cget("text"),
        Go_back_1.cget("text"),
        Rotate_right_1.cget("text"),
         Rotate_left_1.cget("text"),
         Shoot_1.cget("text"),
        # Player 2
         Go_ahead_2.cget("text"),
         Go_back_2.cget("text"),
         Rotate_right_2.cget("text"),
         Rotate_left_2.cget("text"),
         Shoot_2.cget("text"),
        # Player 3
         Go_ahead_3.cget("text"),
         Go_back_3.cget("text"),
         Rotate_right_3.cget("text"),
         Rotate_left_3.cget("text"),
         Shoot_3.cget("text"),
        # Player 4
         Go_ahead_4.cget("text"),
         Go_back_4.cget("text"),
         Rotate_right_4.cget("text"),
         Rotate_left_4.cget("text"),
         Shoot_4.cget("text")
    ]
    if event.keycode >= 96 and event.keycode <= 111:
        key = "Np_" + key
    if key in coppy_states:
            messagebox.showerror("Key Error", f"Key '{key}' is already assigned to another button")
    else:
        button.config(text=key)





controller_frame = tk.Frame(my_canvas)

#player 1
controller1_label = ttk.LabelFrame(controller_frame, text="Controller1 Settings",height=100,padding=1.5)
controller1_label.pack()
Go_ahead_label_1=ttk.LabelFrame(controller1_label,text="Go straight",width=5,height=5)
Go_ahead_label_1.grid(row=0,column=0)
Go_ahead_1=Button(Go_ahead_label_1,text=button_states[0],width=7, height=1)
Go_ahead_1.pack()
Go_ahead_1.bind("<Button-1>",lambda e: received_but(Go_ahead_1))
Go_back_label_1=ttk.LabelFrame(controller1_label,text="   Go back",width=5,height=5)
Go_back_label_1.grid(row=0,column=1)
Go_back_1=Button(Go_back_label_1,text=button_states[1],width=7,height=1)
Go_back_1.pack()
Go_back_1.bind("<Button-1>",lambda e:received_but(Go_back_1))
Rotate_right_label_1=ttk.LabelFrame(controller1_label,text="Rotate Right",width=5,height=5)
Rotate_right_label_1.grid(row=0,column=2)
Rotate_right_1=Button(Rotate_right_label_1,text=button_states[2],width=7,height=1)
Rotate_right_1.pack()
Rotate_right_1.bind("<Button-1>",lambda e:received_but(Rotate_right_1))
Rotate_left_label_1=ttk.LabelFrame(controller1_label,text="Rotate Left",width=5,height=5)
Rotate_left_label_1.grid(row=0,column=3)
Rotate_left_1=Button(Rotate_left_label_1,text=button_states[3],width=7,height=1)
Rotate_left_1.pack()
Rotate_left_1.bind("<Button-1>",lambda e:received_but(Rotate_left_1))
Shoot_label_1=ttk.LabelFrame(controller1_label,text="  Shoot",width=5,height=5)
Shoot_label_1.grid(row=0,column=4)
Shoot_1=Button(Shoot_label_1,text=button_states[4],width=7,height=1)
Shoot_1.pack()
Shoot_1.bind("<Button-1>",lambda  e:received_but(Shoot_1))

#player 2
controller2_label = ttk.LabelFrame(controller_frame, text="Controller2 Settings",height=100,padding=1.5)
controller2_label.pack()
Go_ahead_label_2=ttk.LabelFrame(controller2_label,text="Go straight",width=5,height=5)
Go_ahead_label_2.grid(row=0,column=0)
Go_ahead_2=Button(Go_ahead_label_2,text=button_states[5],width=7, height=1)
Go_ahead_2.pack()
Go_ahead_2.bind("<Button-1>",lambda e: received_but(Go_ahead_2))
Go_back_label_2=ttk.LabelFrame(controller2_label,text="   Go back",width=5,height=5)
Go_back_label_2.grid(row=0,column=1)
Go_back_2=Button(Go_back_label_2,text=button_states[6],width=7,height=1)
Go_back_2.pack()
Go_back_2.bind("<Button-1>",lambda e:received_but(Go_back_2))
Rotate_right_label_2=ttk.LabelFrame(controller2_label,text="Rotate Right",width=5,height=5)
Rotate_right_label_2.grid(row=0,column=2)
Rotate_right_2=Button(Rotate_right_label_2,text=button_states[7],width=7,height=1)
Rotate_right_2.pack()
Rotate_right_2.bind("<Button-1>",lambda e:received_but(Rotate_right_2))
Rotate_left_label_2=ttk.LabelFrame(controller2_label,text="Rotate Left",width=5,height=5)
Rotate_left_label_2.grid(row=0,column=3)
Rotate_left_2=Button(Rotate_left_label_2,text=button_states[8],width=7,height=1)
Rotate_left_2.pack()
Rotate_left_2.bind("<Button-1>",lambda e:received_but(Rotate_left_2))
Shoot_label_2=ttk.LabelFrame(controller2_label,text="  Shoot",width=5,height=5)
Shoot_label_2.grid(row=0,column=4)
Shoot_2=Button(Shoot_label_2,text=button_states[9],width=7,height=1)
Shoot_2.pack()
Shoot_2.bind("<Button-1>",lambda  e:received_but(Shoot_2))


#player 3
controller3_label = ttk.LabelFrame(controller_frame, text="Controller3 Settings",height=100,padding=1.5)
controller3_label.pack()
Go_ahead_label_3=ttk.LabelFrame(controller3_label,text="Go straight",width=5,height=5)
Go_ahead_label_3.grid(row=0,column=0)
Go_ahead_3=Button(Go_ahead_label_3,text=button_states[10],width=7, height=1)
Go_ahead_3.pack()
Go_ahead_3.bind("<Button-1>",lambda e: received_but(Go_ahead_3))
Go_back_label_3=ttk.LabelFrame(controller3_label,text="   Go back",width=5,height=5)
Go_back_label_3.grid(row=0,column=1)
Go_back_3=Button(Go_back_label_3,text=button_states[11],width=7,height=1)
Go_back_3.pack()
Go_back_3.bind("<Button-1>",lambda e:received_but(Go_back_3))
Rotate_right_label_3=ttk.LabelFrame(controller3_label,text="Rotate Right",width=5,height=5)
Rotate_right_label_3.grid(row=0,column=2)
Rotate_right_3=Button(Rotate_right_label_3,text=button_states[12],width=7,height=1)
Rotate_right_3.pack()
Rotate_right_3.bind("<Button-1>",lambda e:received_but(Rotate_right_3))
Rotate_left_label_3=ttk.LabelFrame(controller3_label,text="Rotate Left",width=5,height=5)
Rotate_left_label_3.grid(row=0,column=3)
Rotate_left_3=Button(Rotate_left_label_3,text=button_states[13],width=7,height=1)
Rotate_left_3.pack()
Rotate_left_3.bind("<Button-1>",lambda e:received_but(Rotate_left_3))
Shoot_label_3=ttk.LabelFrame(controller3_label,text="  Shoot",width=5,height=5)
Shoot_label_3.grid(row=0,column=4)
Shoot_3=Button(Shoot_label_3,text=button_states[14],width=7,height=1)
Shoot_3.pack()
Shoot_3.bind("<Button-1>",lambda  e:received_but(Shoot_3))

#player 4
controller4_label = ttk.LabelFrame(controller_frame, text="Controller4 Settings",height=100,padding=1.5)
controller4_label.pack()
Go_ahead_label_4=ttk.LabelFrame(controller4_label,text="Go straight",width=5,height=5)
Go_ahead_label_4.grid(row=0,column=0)
Go_ahead_4=Button(Go_ahead_label_4,text=button_states[15],width=7, height=1)
Go_ahead_4.pack()
Go_ahead_4.bind("<Button-1>",lambda e: received_but(Go_ahead_4))
Go_back_label_4=ttk.LabelFrame(controller4_label,text="   Go back",width=5,height=5)
Go_back_label_4.grid(row=0,column=1)
Go_back_4=Button(Go_back_label_4,text=button_states[16],width=7,height=1)
Go_back_4.pack()
Go_back_4.bind("<Button-1>",lambda e:received_but(Go_back_4))
Rotate_right_label_4=ttk.LabelFrame(controller4_label,text="Rotate Right",width=5,height=5)
Rotate_right_label_4.grid(row=0,column=2)
Rotate_right_4=Button(Rotate_right_label_4,text=button_states[17],width=7,height=1)
Rotate_right_4.pack()
Rotate_right_4.bind("<Button-1>",lambda e:received_but(Rotate_right_4))
Rotate_left_label_4=ttk.LabelFrame(controller4_label,text="Rotate Left",width=5,height=5)
Rotate_left_label_4.grid(row=0,column=3)
Rotate_left_4=Button(Rotate_left_label_4,text=button_states[18],width=7,height=1)
Rotate_left_4.pack()
Rotate_left_4.bind("<Button-1>",lambda e:received_but(Rotate_left_4))
Shoot_label_4=ttk.LabelFrame(controller4_label,text="  Shoot",width=5,height=5)
Shoot_label_4.grid(row=0,column=4)
Shoot_4=Button(Shoot_label_4,text=button_states[19],width=7,height=1)
Shoot_4.pack()
Shoot_4.bind("<Button-1>",lambda  e:received_but(Shoot_4))

root.mainloop()
