from tkinter import Canvas, PhotoImage


class TkCanvas:
    _board = None
    _parent = None
    _name_id = ""
    _objects = {}

    def __init__(self, parent, name_id, options=None):
        if options is None:
            options = {}
        self._board = Canvas(parent.getWindow(), options)
        self._parent = parent
        self._name_id = name_id
        self._parent.newCanvas(name_id, self._board)

    def getBoard(self):
        return self._board

    def getItem(self, name_id):
        return self._board[name_id]

    # OBJECTS ----------------------------------------------------------------------

    def image(self, x1, y1, image, options={}):
        options["image"] = PhotoImage(file=image)
        return self._board.create_image(x1, y1, options)

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
