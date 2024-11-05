from tkinter import Label, Tk, Canvas, OptionMenu, StringVar, messagebox
import pytz 
from datetime import datetime
import random


app_window = Tk()
app_window.title("Digital Clock")
app_window.attributes('-fullscreen', True)
app_window.bind("<Escape>", lambda e: app_window.attributes('-fullscreen', False))


text_font = ("Boulder", 80, 'bold')
message_font = ("Arial", 24)
foreground = "#ffffff"
background_colors = ["#2c3e50", "#3498db", "#e74c3c", "#2ecc71", "#f1c40f", "#8e44ad"]


canvas = Canvas(app_window, bg=background_colors[0])
canvas.pack(fill="both", expand=True)


label_clock = Label(canvas, font=text_font, fg=foreground, bg=background_colors[0])
label_date = Label(canvas, font=message_font, fg=foreground, bg=background_colors[0])
label_timezone = Label(canvas, text="Select Time Zone:", font=message_font, fg=foreground, bg=background_colors[0])


label_clock.place(relx=0.5, rely=0.3, anchor='center')
label_date.place(relx=0.5, rely=0.4, anchor='center')
label_timezone.place(relx=0.5, rely=0.55, anchor='center')


time_zones = {
    "India": "Asia/Kolkata",
    "USA (New York)": "America/New_York",
    "UK": "Europe/London",
    "Japan": "Asia/Tokyo",
    "Australia (Sydney)": "Australia/Sydney"
}


selected_time_zone = StringVar(app_window, value="India")  


option_menu = OptionMenu(app_window, selected_time_zone, *time_zones.keys())
option_menu.config(font=message_font)
option_menu.place(relx=0.5, rely=0.65, anchor='center')

def change_background():
    new_color = random.choice(background_colors)
    canvas.config(bg=new_color)
    for widget in [label_clock, label_date, label_timezone, option_menu]:
        widget.config(bg=new_color)
    app_window.after(5000, change_background)

def show_alert():
    messagebox.showinfo("Time Alert", "HEY PLEASE DRINK WATER")


is_first_update = True

def update_clock():
    global is_first_update  

    tz_name = time_zones[selected_time_zone.get()]
    local_time = datetime.now(pytz.timezone(tz_name))

    label_clock.config(text=local_time.strftime('%I:%M:%S %p'))
    label_date.config(text=f"Date: {local_time.strftime('%Y-%m-%d')}")

    
    if not is_first_update and local_time.second % 10 == 0:
        show_alert()

    is_first_update = False  
    
    label_clock.after(1000, update_clock)


change_background()
update_clock()

app_window.mainloop()