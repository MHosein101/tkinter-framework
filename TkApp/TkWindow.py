from tkinter import *


class TkWindow:
    _window = None
    _title = 'Window Title'
    _size = (50, 50)

    _menu = {
        "main": None,
        "sub": {}
    }

    _containers = {}
    _widgets = {}

    _packageDesignLayout = False
    _layoutSchema = None
    _userDesignLayout = False

    # WINDOW ----------------------------------------------------------------------

    def __init__(self, title="", size=None):
        self._window = Tk()
        if title != "":
            self._title = title
        if size is not None:
            self._size = size
        self._window.title(self._title)
        self._window.geometry(f"{self._size[0]}x{self._size[1]}")

    def getWindow(self):
        return self._window

    def getMenu(self):
        return self._menu["main"]

    def getSubMenu(self):
        return self._menu["child"]

    def getContainer(self, frame_name):
        return self._containers[frame_name]

    def getContainersCount(self):
        return len(self._containers)

    def getWidget(self, widget_name):
        return self._widgets[widget_name]

    def getWidgetsCount(self):
        return len(self._widgets)

    # WIDGETS ----------------------------------------------------------------------

    def newWidget(self, name_id, widget_object):
        self._widgets[name_id] = widget_object
        return self

    def newButton(self, name_id, options):
        self._widgets[name_id] = Button(self._window, options)
        return self

    def newLabel(self, name_id, options):
        self._widgets[name_id] = Label(self._window, options)
        return self

    def newText(self, name_id, options):
        self._widgets[name_id] = Message(self._window, options)
        return self

    def newInput(self, name_id, options):
        self._widgets[name_id] = Entry(self._window, options)
        return self

    def newTextbox(self, name_id, options):
        self._widgets[name_id] = Text(self._window, options)
        return self

    def newCheck(self, name_id, options):
        self._widgets[name_id] = Checkbutton(self._window, options)
        return self

    def newRadio(self, name_id, options):
        self._widgets[name_id] = Radiobutton(self._window, options)
        return self

    def newSpin(self, name_id, options):
        self._widgets[name_id] = Spinbox(self._window, options)
        return self

    def newCanvas(self, name_id, canvas):
        from TkApp.TkCanvas import TkCanvas
        if isinstance(canvas, TkCanvas):
            self._widgets[name_id] = canvas.getBoard()
        else:
            self._widgets[name_id] = canvas
        return self

    def newList(self, name_id, options):
        self._widgets[name_id] = Listbox(self._window, options)
        return self

    def newFrame(self, name_id, container):
        self._containers[name_id] = container
        self._widgets[name_id] = container
        return self

    def newGroup(self, name_id, group):
        self._widgets[name_id] = group
        return self

    # EVENTS ----------------------------------------------------------------------

    def onEvent(self, widget_name, event_name, event_listener, *args):
        if len(args) > 0:
            self._widgets[widget_name].bind(event_name, lambda e: event_listener(e, *args))
        else:
            self._widgets[widget_name].bind(event_name, event_listener)
        return self

    def onClick(self, widget_name, event_listener, *args):
        if len(args) > 0:
            self._widgets[widget_name].bind("<Button-1>", lambda e: event_listener(self, e, *args))
        else:
            self._widgets[widget_name].bind("<Button-1>", event_listener)
        return self

    def onDblClick(self, widget_name, event_listener, *args):
        if len(args) > 0:
            self._widgets[widget_name].bind("<Double-Button-1>", lambda e: event_listener(self, e, *args))
        else:
            self._widgets[widget_name].bind("<Double-Button-1>", event_listener)
        return self

    def onFocusIn(self, widget_name, event_listener, *args):
        if len(args) > 0:
            self._widgets[widget_name].bind("<FocusIn>", lambda e: event_listener(self, e, *args))
        else:
            self._widgets[widget_name].bind("<FocusIn>", event_listener)
        return self

    def onFocusOut(self, widget_name, event_listener, *args):
        if len(args) > 0:
            self._widgets[widget_name].bind("<FocusOut>", lambda e: event_listener(self, e, *args))
        else:
            self._widgets[widget_name].bind("<FocusOut>", event_listener)
        return self

    def onKeyPress(self, widget_name, event_listener, *args):
        self._widgets[widget_name].bind("<Key>", event_listener)
        if len(args) > 0:
            self._widgets[widget_name].bind("<Double-Button-1>", lambda e: event_listener(self, e, *args))
        else:
            self._widgets[widget_name].bind("<Double-Button-1>", event_listener)
        return self

    def onEnter(self, widget_name, event_listener, *args):
        if len(args) > 0:
            self._widgets[widget_name].bind("<Enter>", lambda e: event_listener(self, e, *args))
        else:
            self._widgets[widget_name].bind("<Enter>", event_listener)
        return self

    def onLeave(self, widget_name, event_listener, *args):
        if len(args) > 0:
            self._widgets[widget_name].bind("<Leave>", lambda e: event_listener(self, e, *args))
        else:
            self._widgets[widget_name].bind("<Leave>", event_listener)
        return self

    # WIDGET CONFIGS ----------------------------------------------------------------------

    def windowConfig(self, options):
        self._window.config(options)

    def config(self, widget_name, options):
        self._widgets[widget_name].config(options)

    def pack(self, widget_name, options):
        self._widgets[widget_name].pack(options)

    def grid(self, widget_name, options):
        self._widgets[widget_name].grid(options)

    def place(self, widget_name, options):
        self._widgets[widget_name].place(options)

    # WINDOW UI ----------------------------------------------------------------------

    def setMenu(self, template):
        appMenu = Menu(self._window)
        menuItems = {}
        for title, itemsList in template.items():
            menuItems[title] = Menu(appMenu, tearoff=0)
            for item in itemsList:
                if item["type"] == "command":
                    menuItems[title].add_command(item["options"])
                elif item["type"] == "radio":
                    menuItems[title].add_radiobutton(item["options"])
                elif item["type"] == "check":
                    menuItems[title].add_checkbutton(item["options"])
                elif item["type"] == "-":
                    menuItems[title].add_separator()
            appMenu.add_cascade({
                "label": title,
                "menu": menuItems[title]
            })
        self._window.config({"menu": appMenu})
        self._menu["main"] = appMenu
        self._menu["sub"] = menuItems

    def userDesign(self, action=True):
        self._userDesignLayout = action

    def createLayout(self, pattern):
        self._packageDesignLayout = True
        self._layoutSchema = pattern

    def start(self):
        if self._userDesignLayout:
            self._window.mainloop()
        elif self._packageDesignLayout:
            i = 0
            perRow = self._size[1] / len(self._layoutSchema)
            for row in self._layoutSchema:
                if len(row) > 0:
                    rowIndex = i
                    perBlock = self._size[0] / len(row)
                    for column in row:
                        if column != 0:
                            xPos = (perBlock * row.index(column)) - (perBlock / 3)
                            if xPos < 0:
                                xPos = 0
                            yPos = (perRow * rowIndex) - (perRow / 3)
                            if yPos > self._size[1]:
                                yPos = self._size[1] - column.config()["width"]
                            self._widgets[column].place(x=xPos, y=yPos)
                i += 1
            self._window.mainloop()
        else:
            for widget_name in self._widgets:
                self._widgets[widget_name].pack()
            self._window.mainloop()

    def minimize(self):
        self._window.iconify()

    def minSize(self, minW, minH):
        self._window.minsize(minW, minH)

    def maxSize(self, maxW, maxH):
        self._window.maxsize(maxW, maxH)

    def exit(self):
        self._window.quit()
