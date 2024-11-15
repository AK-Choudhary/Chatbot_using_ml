import subprocess
import os

def launch_chatbot():
    # Command to open a new terminal window and run the Chatbot.py script
    command = "start cmd /k python c:\\Users\\ENVY\\Documents\\Pandas\\Chatbot.py"
    subprocess.Popen(command, shell=True)

if __name__ == "__main__":
    launch_chatbot()
