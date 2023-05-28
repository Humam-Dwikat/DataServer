class Config:
    def __init__(self, host: str = 'localhost', port: int = 9200):
        self.db_host = host
        self.port = port