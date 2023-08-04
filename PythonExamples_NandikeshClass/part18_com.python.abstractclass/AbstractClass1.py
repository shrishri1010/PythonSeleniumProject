#abc is Abstract baseclass. From this baseclass importing ABC module and abstractmethod
from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def displaybluetooth(self):
        None

    #non abstract method
    def wifi(self):
        print('method 2')

    def hotspot(self):
        print('method 3')

class B(A):
    def displaybluetooth(self):
        print('this is display method')
b=B()
b.displaybluetooth()
b.wifi()
b.hotspot()













