from dbson.data_types import Object, Associative
from dbson.deserializer import deserialize
from dbson.serializer import serialize
import dbson.commands as commands
from typing import Union
import socket


class Client:

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def execute(self, command: Object) -> Object:
        return self.send(command)

    def set(self, *, collection_name: Union[str, Associative],
            object_name: Union[str, Associative],
            selector: str = "", **kwargs):
        command = commands.construct_set(collection_name=collection_name,
                                         object_name=object_name,
                                         selector=selector, **kwargs)
        return self.execute(command)

    def get(self, *, collection_name: Union[str, Associative],
            object_name: Union[str, Associative],
            selector: str = "", **kwargs):
        command = commands.construct_get(collection_name=collection_name,
                                         object_name=object_name,
                                         selector=selector, **kwargs)
        return self.execute(command)

    def ping(self, **kwargs):
        return self.execute(commands.construct_ping(**kwargs))

    def send(self, data: Object) -> Object:
        return self.send_one_tcp(data)

    def send_one_tcp(self, data: Object) -> Object:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            buffered_io = s.makefile('wrb')
            serialize(data, buffered_io)
            buffered_io.flush()
            result = deserialize(buffered_io)
            buffered_io.flush()
            s.close()
        return result


def connect(host: str, port: int) -> Client:
    client = Client(host, port)
    response = client.ping()
    if response.get(commands.SUCCESS_LABEL, False) != True:
        raise ConnectionError('ping command failed')
    return client
