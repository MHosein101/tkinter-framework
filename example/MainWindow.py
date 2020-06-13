# Importing module
from TkApp import *

# Make a class for window UI and inharite from AppWindow class inside TkApp package
class MainWindowMaker(AppWindow):
    # Set the window title and resolution as tuple items
    _window_props = ("Painting With Tkinter", (500, 300))

    # Custome variable for working
    __board = None

    # Override this method to setup some window ui widgets
    def setupUi(self, win):
        self.__board = TkCanvas(win, "board")
        win.pack("board", {
            "expand": PyTk.YES,
            "fill": PyTk.BOTH
        })
        win.newLabel("l1", {
            "text": "Press and Drag the mouse to draw"
        }).pack("l1", {
            "side": PyTk.BOTTOM
        })

    # Override this method to bind event listeners to widgets
    def setupEvents(self, win):
        win.onEvent("board", "<B1-Motion>", self.setHandler("try_to_draw"), self.__board)

# Custome event controller class
class MainWindowController:
    # Method that listen for event
    def try_to_draw(self, e, board):
        x1 = e.x - 5
        y1 = e.y - 5
        x2 = e.x + 5
        y2 = e.y + 5
        board.line((x1, y1, x2, y2), {"fill": "#476042"})
