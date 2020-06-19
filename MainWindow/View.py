from TkApp import *


class View(AppWindow):
    _window_props = ("Painting With Tkinter", (500, 300))

    canvas_board = None

    # Initialize Widgets In Window
    def setupUi(self, window):
        self.canvas_board = TkCanvas(window, "board")
        window.newLabel("l1", {
            "text": "Press and Drag the mouse to draw"
        })

    # Set Widgets Positions In Window
    def setupPositions(self, window):
        window.pack("board", {
            "expand": PyTk.YES,
            "fill": PyTk.BOTH
        })
        window.pack("l1", {
            "side": PyTk.BOTTOM
        })

    # Add Event Handler To Widget
    def setupEvents(self, window):
        window.onEvent("board", "<B1-Motion>", self.getHandler("try_to_draw"), self.canvas_board)

    # Create Menu From Template
    def setupMenu(self):
        return {
            "File": [
                {
                    "type": "command",
                    "options": {
                        "label": "Exit",
                        "command": self.getHandler("menu_file_exit")
                    }
                }
            ]
        }
