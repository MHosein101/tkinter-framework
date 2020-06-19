from tkinter import *


class TkGroup:
    _group = None
    _widgets = {}
    _parent = None
    _name_id = ""

    # ----------------------------------------------------------------------

    def __init__(self, name_id, parent, options=None):
        if options is None:
            options = {}
        self._group = LabelFrame(parent.getWindow(), options)
        self._parent = parent
        self._name_id = name_id
        self._parent.newGroup(name_id, self._group)

    def getGroup(self):
        return self._group

    def getWidget(self, widget_name):
        return self._parent.getWidget(widget_name)

    def getWidgetsCount(self, widget_name):
        return len(self._parent.getWidgetsCount(widget_name))

    # WIDGET CONFIGS ----------------------------------------------------------------------

    def thisConfig(self, options=None):
        if options is None:
            options = {}
        self._parent.getWidget(self._name_id).config(options)

    def thisPack(self, options=None):
        if options is None:
            options = {}
        self._parent.getWidget(self._name_id).pack(options)

    def thisGrid(self, options=None):
        if options is None:
            options = {}
        self._parent.getWidget(self._name_id).grid(options)

    def thisPlace(self, options=None):
        if options is None:
            options = {}
        self._parent.getWidget(self._name_id).place(options)

    def config(self, name_id, options=None):
        if options is None:
            options = {}
        self._parent.getWidget(name_id).config(options)

    def pack(self, name_id, options=None):
        if options is None:
            options = {}
        self._parent.getWidget(name_id).pack(options)

    def grid(self, name_id, options=None):
        if options is None:
            options = {}
        self._parent.getWidget(name_id).grid(options)

    def place(self, name_id, options=None):
        if options is None:
            options = {}
        self._parent.getWidget(name_id).place(options)

    # ----------------------------------------------------------------------

    def newWidget(self, name_id, widget_object):
        self._parent.newWidget(name_id, widget_object)
        self._widgets[name_id] = widget_object
        return self

    def newButton(self, name_id, options):
        btn = Button(self._group, options)
        self._parent.newWidget(name_id, btn)
        self._widgets[name_id] = btn
        return self

    def newLabel(self, name_id, options):
        lbl = Label(self._group, options)
        self._parent.newWidget(name_id, lbl)
        self._widgets[name_id] = lbl
        return self

    def newText(self, name_id, options):
        msg = Message(self._group, options)
        self._parent.newWidget(name_id, msg)
        self._widgets[name_id] = msg
        return self

    def newInput(self, name_id, options):
        ntr = Entry(self._group, options)
        self._parent.newWidget(name_id, ntr)
        self._widgets[name_id] = ntr
        return self

    def newTextbox(self, name_id, options):
        txtbx = Text(self._group, options)
        self._parent.newWidget(name_id, txtbx)
        self._widgets[name_id] = txtbx
        return self

    def newCheck(self, name_id, options):
        chckbtn = Checkbutton(self._group, options)
        self._parent.newWidget(name_id, chckbtn)
        self._widgets[name_id] = chckbtn
        return self

    def newRadio(self, name_id, options):
        rdbtn = Radiobutton(self._group, options)
        self._parent.newWidget(name_id, rdbtn)
        self._widgets[name_id] = rdbtn
        return self

    def newSpin(self, name_id, options):
        spn = Spinbox(self._group, options)
        self._parent.newWidget(name_id, spn)
        self._widgets[name_id] = spn
        return self

    def newCanvas(self, name_id, canvas):
        from TkApp.TkCanvas import TkCanvas
        if isinstance(canvas, TkCanvas):
            self._parent.newWidget(name_id, canvas.getBoard())
            self._widgets[name_id] = canvas.getBoard()
        else:
            self._parent.newWidget(name_id, canvas)
            self._widgets[name_id] = canvas
        return self

    def newList(self, name_id, options):
        lstbx = Listbox(self._group, options)
        self._parent.newWidget(name_id, lstbx)
        self._widgets[name_id] = lstbx
        return self