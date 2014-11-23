import kivy
kivy.require('1.0.9')
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
from kivy.properties import NumericProperty
from kivy.app import App
from kivy.clock import Clock
import test.regrtest

PASSED = test.regrtest.PASSED

STDTESTS = [
    'test_grammar',
    'test_opcodes',
    'test_dict',
    'test_builtin',
    'test_exceptions',
    'test_types',
    'test_unittest',
    'test_socket',
    'test_ctypes',
]

# 'test_doctest',
# 'test_doctest2',

testVerbose = True
testQuiet = False

class MainScreen(GridLayout):
    totalNumberOfTests = len(STDTESTS)
    currentTestNumber = 0
    currentTestName = ""
    pb = ProgressBar(max=totalNumberOfTests)

    while(currentTestNumber < totalNumberOfTests):
        currentTestName = STDTESTS[currentTestNumber]
        result, duration = test.regrtest.runtest(currentTestName, testVerbose, testQuiet)
        if result == PASSED:
            pass
        else:
            print "'%s' failed - code == %d" % (currentTestName, result)
        currentTestNumber += 1
        pb.value = currentTestNumber

class HelloWorldApp(App):
    def build(self):
        mainScreen = MainScreen()
        return mainScreen

if __name__ == '__main__':
    HelloWorldApp().run()