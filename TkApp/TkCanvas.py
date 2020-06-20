from tkinter import Canvas, PhotoImage


class TkCanvas:
    _board = None
    _parent = None
    _name_id = ""

    def __init__(self, parent, name_id, options=None):
        if options is None:
            options = {}
        self._board = Canvas(parent.getWindow(), options)
        self._parent = parent
        self._name_id = name_id
        self._parent.newCanvas(name_id, self._board)

    def getBoard(self):
        return self._board

    # OBJECTS ----------------------------------------------------------------------

    def arc(self, coords, options={}):
        return self._board.create_arc(coords, options)

    def oval(self, coords, options={}):
        return self._board.create_oval(coords, options)

    def polygon(self, coords, options={}):
        return self._board.create_polygon(coords, options)

    def line(self, coords, options={}):
        return self._board.create_line(coords, options)

    def text(self, x1, y1, text, options={}):
        options["text"] = text
        return self._board.create_text(x1, y1, options)
