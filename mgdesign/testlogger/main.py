import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.app import App
import logging
import mobileLogging

Builder.load_string('''
<HelloWorldScreen>:
    cols: 1
    Label:
        text: 'Welcome to the Hello world'
    Button:
        text: 'Click me! %d' % root.counter
        on_release: root.my_callback()
''')

class HelloWorldScreen(GridLayout):
    counter = NumericProperty(0)

    # Register our custom tcp Logger class
    logging.setLoggerClass( mobileLogging.TcpLogger )

    # Now, instanciate a couple of loggers:
    logger1 = logging.getLogger('Android.log')

    # Connect to log server
    logger1.connect('192.168.0.117')    
    
    def my_callback(self):
        print 'The button have been pushed'
        self.counter += 1
        self.logger1.warning('Button pushed from Android (%d times)!', self.counter)

class HelloWorldApp(App):
    def build(self):
        return HelloWorldScreen()

if __name__ == '__main__':
    HelloWorldApp().run()