

class MyClass(object):

    def __init__(self, prop):
        self.prop = prop

    def some_method(self, num, string):
        print('method:', num, string)

def listener_method(obj, num, string):
    print('listener:', num, string, obj.prop)

my = MyClass('my_prop')

add_listener(my, 'first_method', listener_method)
my.some_method(42, 'with listener')

remove_listener(my, 'first_method', listener_method)
my.some_method(42, 'without listener')

And the output is:

method: 42 with listener
listener: 42 with listener my_prop
method: 42 without listener

