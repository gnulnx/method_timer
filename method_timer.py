# Copy this somewhere and use it.
#
# @method_timer(name='method_name_for_reporting')
# def blah():

class method_timer(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            start = time()
            result = f(*args, **kwargs)
            end = time()
            print '{} - Elapsed time: {}'.format(self.name, end-start)
            return result
        return wrapper
