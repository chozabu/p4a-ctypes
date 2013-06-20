import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.app import App
from ctypes import *

Builder.load_string('''
<HelloWorldScreen>:
    cols: 1
    Label:
        text: 'Welcome to the Python _ctypes world\\nPython version %s' % root.pyversion
    Button:
        text: 'Click me! %d' % root.counter
        on_release: root.my_callback()
''')

class HelloWorldScreen(GridLayout):
    counter = NumericProperty(0)
    pyversion = ""
    libpython=cdll.LoadLibrary('libpython2.7.so')
    getpythonversion = libpython.Py_GetVersion
    getpythonversion.restype = c_char_p
    pyversion = getpythonversion()
    def my_callback(self):
        print 'The button have been pushed'
        self.counter += 1

class HelloWorldApp(App):
    def build(self):
        return HelloWorldScreen()

if __name__ == '__main__':
    HelloWorldApp().run()