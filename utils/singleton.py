class Singleton:
    __instances = {}
    def __new__(cls, **kwargs):
        if not cls.__name__ in Singleton.__instances:
            new_instance = super().__new__(cls)
            for key, value in kwargs.items():
                setattr(new_instance, key, value)
            Singleton.__instances[cls.__name__] = new_instance
        return Singleton.__instances[cls.__name__]
