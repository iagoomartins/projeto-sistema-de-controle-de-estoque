# configuração do banco de dados


class Config:
    SECRET_KEY = 'CUGOZADOPSOJAMTR904JN40IF0AJMRIKOPE'
   # SECRET_KEY = os.environ.get('bucetagozada') 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///estoque.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False