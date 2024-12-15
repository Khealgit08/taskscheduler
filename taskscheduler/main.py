# Main entry point of the application
from tkinter import Tk
from taskscheduler.ui import TaskSchedulerApp

def main():
    root = Tk()
    app = TaskSchedulerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
