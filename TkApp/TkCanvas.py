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

    # BOARD EVENTS ----------------------------------------------------------------------

    def onEvent(self, event_name, event_listener):
        self._parent.getWidget(self._name_id).bind(event_name, event_listener)
        return self

    def onClick(self, event_listener):
        self._parent.getWidget(self._name_id).bind("<Button-1>", event_listener)
        return self

    def onDblClick(self, event_listener):
        self._parent.getWidget(self._name_id).bind("<Double-Button-1>", event_listener)
        return self

    def onFocusIn(self, event_listener):
        self._parent.getWidget(self._name_id).bind("<FocusIn>", event_listener)
        return self

    def onFocusOut(self, event_listener):
        self._parent.getWidget(self._name_id).bind("<FocusOut>", event_listener)
        return self

    def onKeyPress(self, event_listener):
        self._parent.getWidget(self._name_id).bind("<Key>", event_listener)
        return self

    def onEnter(self, event_listener):
        self._parent.getWidget(self._name_id).bind("<Enter>", event_listener)
        return self

    def onLeave(self, event_listener):
        self._parent.getWidget(self._name_id).bind("<Leave>", event_listener)
        return self

    # OBJECTS EVENTS ----------------------------------------------------------------------

    def onObjectEvent(self, object_id, event_name, event_listener):
        self._parent.getWidget(object_id).bind(event_name, event_listener)
        return self

    def onObjectClick(self, object_id, event_listener):
        self._parent.getWidget(object_id).bind("<Button-1>", event_listener)
        return self

    def onObjectDblClick(self, object_id, event_listener):
        self._parent.getWidget(object_id).bind("<Double-Button-1>", event_listener)
        return self

    def onObjectFocusIn(self, object_id, event_listener):
        self._parent.getWidget(object_id).bind("<FocusIn>", event_listener)
        return self

    def onObjectFocusOut(self, object_id, event_listener):
        self._parent.getWidget(object_id).bind("<FocusOut>", event_listener)
        return self

    def onObjectKeyPress(self, object_id, event_listener):
        self._parent.getWidget(object_id).bind("<Key>", event_listener)
        return self

    def onObjectEnter(self, object_id, event_listener):
        self._parent.getWidget(object_id).bind("<Enter>", event_listener)
        return self

    def onObjectLeave(self, object_id, event_listener):
        self._parent.getWidget(object_id).bind("<Leave>", event_listener)
        return self
