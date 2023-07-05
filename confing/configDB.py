class Config:
    """
    This class contains the main parameters that I need in my app
    """
    __instance = None

    def __init__(self, __private: bool = False, host: str = '0.0.0.0:9200'):
        self.db_host = host

        self.__instance = self
        if not __private:
            raise ("Can't be instantiated through the constructor,"
                   " Use .get_instance() instead")

    @classmethod
    def get_instance(cls) -> 'Config':
        """
        use the Singleton pattern to create an instance from config
        """
        if cls.__instance is None:
            cls.__instance = cls(True)
        return cls.__instance
