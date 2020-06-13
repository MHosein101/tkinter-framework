from TkApp import *


class AppWindow:
    _window_props = {}
    _controller = None
    _app_window = None

    def __init__(self, event_controller):
        self._controller = event_controller()
        self._app_window = TkWindow(self._window_props[0], self._window_props[1])
        self.setupUi(self._app_window)
        self.setupEvents(self._app_window)
        self._app_window.start()

    def setupUi(self, window):
        # for useing event handlers -> self.setHandler("login_btn_click")
        pass

    def setupEvents(self, window):
        pass

    def setHandler(self, name):
        return getattr(self._controller, name)

    def window(self):
        return self._app_window

    def exit(self, win):
        if isinstance(win, TkWindow):
            win.exit()
        else:
            win.quit()
