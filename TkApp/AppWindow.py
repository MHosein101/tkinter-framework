from TkApp import *


class AppWindow:
    _window_props = ()
    _controller = None
    _app_window = None
    _menu = None

    def __init__(self, event_controller):
        self._controller = event_controller()

        if hasattr(self._controller, "beforeCreate"):
            getattr(self._controller, "beforeCreate")()

        self._app_window = TkWindow(self._window_props[0], self._window_props[1])

        if hasattr(self._controller, "beforeInit"):
            getattr(self._controller, "beforeInit")(self._app_window)

        self.setupUi(self._app_window)
        self.setupEvents(self._app_window)
        self.setupPositions(self._app_window)
        self._app_window.setMenu(self.setupMenu())

        self._controller.view = self
        self._controller.window = self._app_window

        if hasattr(self._controller, "beforeStart"):
            getattr(self._controller, "beforeStart")(self, self._app_window)

        self._app_window.start()

        if hasattr(self._controller, "afterClose"):
            getattr(self._controller, "afterClose")(self, self._app_window)

    def setupUi(self, window):
        pass

    def setupPositions(self, window):
        pass

    def setupEvents(self, window):
        pass

    def setupMenu(self):
        return {}

    def getHandler(self, name):
        if hasattr(self._controller, name):
            return getattr(self._controller, name)

    def window(self):
        return self._app_window

    def rootWindow(self):
        return self._app_window.getWindow()

    def exit(self):
        self._app_window.quit()
