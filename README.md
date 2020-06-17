# Python Tkinter Framework
Simple framework to use python tkinter easily and more readable

## How To Start

imagine you have this project structure<br>
```
/(root)
- /TkApp
- app.py
```
this guide is a best practice for you to organize your codes and diffrent parts of app

now create new folder in root of your project directory
i will call it `MainWindow`
next create to file
- `View.py`
- `Controller.py`

note that you are free to name your classes anything
it is optional and best practice

now you should have this project structure
```
/(root)
- /TkApp
- /MainWindow
- - /View.py
- - /Controller.py
- app.py
```

open `/MainWindow/View.py` and write codes below
```
# /MainWindow/View.py

# import module classes
from TkApp import *
# define a class and inharite from AppWindow parent class
class View(AppWindow):
  pass
```
now you should implement two methods of `AppWindow` class :
1. setupUi(win)<br>
  you should write any code that is for initializing widgets in window here<br>
  and for doing that you have access to `win` variable that is the window object you can work with
2. setupEvents(win)<br>
  you have to set event handlers to window wingets and you have to do it with `win` argument<br>
  also you have to use `self.setHandler("name_of_event_handler")` method to get target event handler 

to set the window title and width and height
you can override `_window_props` atttribute and use it as tuple with two value `("window title", (width,height))` 


now we can extend our `View` class
```
# /MainWindow/View.py

class View(AppWindow):
  _window_props = ("Tk app title", (300,50))
  
  def setupUi(self, win):
    win.newLabel("l1", {
      "text" : "Description Label Text"
    })
    win.pack("l1")
    
  def setupEvents(self, win):
    # you can send extra params to event handler method like below
    win.onClick("l1", self.setHandler("when_label_1_click"), win)
```
and we are done here . now we have to go to `/MainWindow/Controller.py` and define `on_label_click` method
```
# /MainWindow/Controller.py

class Controller:
  def when_label_1_click(event, window):
    window.config("l1", {
      "text" : "You clicked On X : " + event.x + " , Y : " + event.y
    })
```

and finally we should call our main window of application , so in the `/app.py` file
we import `MainWindow` and start the application as below
```
# /app.py

import MainWindow

MainWindow.View(MainWindow.Controller)
```
and enjoy your app :)

i will write more details in future
