class Config:
    __instance = None

    def __init__(self, __private: bool = False, host: str = '0.0.0.0:9200'):
        self.db_host = host

        self.__instance = self
        if not __private:
            raise ("Can't be instantiated through the constructor,"
                   " Use .instance() instead")

    @classmethod
    def instance(cls) -> 'Config':
        if cls.__instance is None:
            cls.__instance = cls(True)
        return cls.__instance
