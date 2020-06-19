from TkApp import *


class AppWindow:
    _window_props = ()
    _controller = None
    _app_window = None

    def __init__(self, event_controller):
        self._controller = event_controller()
        self._app_window = TkWindow(self._window_props[0], self._window_props[1])
        self.setupUi(self._app_window)
        self.setupEvents(self._app_window)
        self.setupPositions(self._app_window)
        self.beforeStart(self._app_window)
        self._app_window.start()
        self.afterStart(self._app_window)

    def setupUi(self, window):
        pass

    def setupPositions(self, window):
        pass

    def setupEvents(self, window):
        pass

    def beforeStart(self, window):
        pass

    def afterStart(self, window):
        pass

    def getHandler(self, name):
        return getattr(self._controller, name)

    def window(self):
        return self._app_window

    def rootWindow(self):
        return self._app_window.getWindow()

    def exit(self, win):
        win.quit()
