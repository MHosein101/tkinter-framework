class Controller:

    # Window Hook (optional)
    def beforeCreate(self):
        print("Before To Create Window")

    # Window Hook (optional)
    def beforeInit(self, window):
        print("After Create Window And Before To Initialize Widgets")

    # Window Hook (optional)
    def beforeStart(self, viewClass, windowObject):
        print("After Initialize Widgets And Before Start App")

    # Window Hook (optional)
    def afterClose(self, viewClass, windowObject):
        print("After App Closed")

    # Canvas Event Handler
    def try_to_draw(self, event, canvas):
        x1 = event.x - 5
        y1 = event.y - 5
        x2 = event.x + 5
        y2 = event.y + 5
        canvas.line((x1, y1, x2, y2), {"fill": "#476042"})

    # Menu Button Clicked
    def menu_file_exit(self):
        # You alson have access to View class and Window object
        # with self.view and self.window properties
        # for example
        self.view.exit()
        # or
        # self.window.quit()

