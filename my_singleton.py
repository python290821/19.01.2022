

# Singleton
# 1. cannot create more than 1 instances
# 2. when getting the object twice (or more) --> we will get the same object every time
# 3. when getting the object from two places at once it will work (later in course)

# hack the __init__

class MySingleton(object):

    # 1
    _instance = None

    # 2
    def __init__(self):
        raise RuntimeError('Call instance() instead')

    # 3
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.name = 'itay' # maybe from config
        return cls._instance

    # @staticmethod
    # def get_instance_static():
    #     if MySingleton._instance is None:
    #         MySingleton._instance = MySingleton.__new__(MySingleton)
    #         MySingleton._instance.name = 'itay'
    #     # check if instance exists
    #     #  ... if not create
    #     # return the instance
    #     return MySingleton._instance

    def print_hello(self):
        print('hello')

sing1 = MySingleton.get_instance()
sing2 = MySingleton.get_instance()
print(sing1 == sing2)
print(sing1)
print(sing2)
print(sing1.name)
sing1.print_hello()
#print(MySingleton._instance)

