# ------------------------------------------------------
# Name:        $ Desktop Notifications.py
# Purpose:       Sens the user a desktop notification when a specified amount of time is over.
# Author:      $ Lalith Sree
# Created:     $ 12/28/2023
# ------------------------------------------------------

import plyer
import customtkinter as ctk


class Timer:
    def __init__(self):
        self.make_win()

    def make_win(self):
        self.root = ctk.CTk()

        self.root._set_appearance_mode('dark')

        self.root.geometry(self.get_app_pos(960, 540))

        self.hour = ctk.CTkEntry(self.root, 300, 65, 10, 1, 'transparent', None, 'grey',
                                 'red', 'black', None, 'Enter the hours', ('Roboto', 20))
        self.hour.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        self.minute = ctk.CTkEntry(self.root, 300, 65, 10, 1, 'transparent', None, 'grey',
                                   'red', 'black', None, 'Enter the minutes', ('Roboto', 20))
        self.minute.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

        self.second = ctk.CTkEntry(self.root, 300, 65, 10, 1, 'transparent', None, 'grey',
                                    'red', 'black', None, 'Enter the minutes', ('Roboto', 20))
        self.second.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

        self.start_button = ctk.CTkButton(self.root, text='Start Timer', font=(
            'Roboto', 50), command=self.timer_init, corner_radius=10)
        self.start_button.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

        self.time_label = ctk.CTkLabel(
            self.root, text_color='#1f6aa5', font=('Roboto', 200), text='')

        self.root.bind('<Return>', self.timer_init_1)
        self.root.mainloop()

    def timer_init_1(self, a):
        self.timer_init()

    def get_app_pos(self, app_width: int, app_height: int) -> str:
        s_w = self.root.winfo_screenwidth()
        s_h = self.root.winfo_screenheight()
        x = s_w // 2 - app_width // 2
        y = s_h // 2 - app_height // 2
        return f'{app_width}x{app_height}+{x}+{y}'

    def timer_init(self):
        self.hours = self.hour.get()
        self.minutes = self.minute.get()
        self.seconds = self.second.get()

        self.h = int(self.hours) if self.hours else 0
        self.m = int(self.minutes) if self.minutes else 0
        self.s = int(self.seconds) if self.seconds else 0

        self.count = self.h*3600 + self.m*60 + self.s

        self.hour.destroy()
        self.minute.destroy()
        self.second.destroy()
        self.start_button.destroy()
        self.time_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.timer()

    def timer(self):

        self.time_label.configure(
            True, text=f"{'0' if len(str(self.h)) == 1 else ''}{self.h}:{'0' if len(str(self.m)) == 1 else ''}{self.m}:{'0' if len(str(self.s)) == 1 else ''}{self.s}")
        id = self.time_label.after(1000, self.timer)
        if self.count == 0:
            notification = plyer.notification
            notification.notify('Timer Ran Out',
                                f"Your Timer for{'' if str(self.hours) == '0' else '0'+str(self.hours) if len (self.hours) == 1 else self.hours}{'hours' if str(self.hours) == '0' else ''}{'' if str(self.minutes) == '0' else '0'+str(self.minutes) if len (self.minutes) == 1 else self.minutes}{'minutes' if not str(self.minutes) == '0' else ''}{'' if str(self.seconds) == '0' else '0'+str(self.seconds) if len (self.seconds) == 1 else self.seconds}{'seconds' if not str(self.seconds) == '0' else ''} ran out.",
                                'Timer', 'media\\time.ico', 5)  # type: ignore

            self.time_label.after_cancel(id)
            self.root.destroy()
        self.count -= 1
        self.s -= 1  # type: ignore
        if self.s == 0 and self.m:
            self.m -= 1  # type: ignore
            self.s += 59
        if self.m == 0 and self.h:
            self.h -= 1  # type: ignore
            self.m += 59  # type:ignore


if __name__ == '__main__':
    T = Timer()
