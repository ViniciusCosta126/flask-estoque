import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:root@localhost:5432/estoque_postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
