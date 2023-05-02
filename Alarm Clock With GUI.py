import tkinter as tk
import time

class AlarmClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alarm Clock")
        self.root.geometry("300x150")
        self.label = tk.Label(self.root, text="", font=("Helvetica", 48))
        self.label.pack(expand=True)
        self.button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.button.pack(expand=True)
        self.alarm_time = None
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.config(text=now)
        if self.alarm_time is not None and now == self.alarm_time:
            self.label.config(text="Time's up!")
            self.alarm_time = None
        self.root.after(1000, self.update_clock)

    def set_alarm(self):
        self.alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
        self.button.config(text="Change Alarm")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    alarm_clock = AlarmClock()
    alarm_clock.run()
