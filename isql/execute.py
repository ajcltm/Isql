from typing import Protocol
import sys
parentPath='c:/Users/ajcltm/PycharmProjects/Isql' # parent 경로
sys.path.append(parentPath)
from isql.connect import IConnection

class IExcuter(Protocol):

    def execute(self, data:dict)->None:
        ...

class Excuter:

    def __init__(self, connector) -> None:
        self.c = connector.cursor()

    def execute(self, sql)->None:
        self.c.execute(sql)
