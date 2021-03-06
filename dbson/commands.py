from typing import Union
from dbson.data_types import Object, Associative

SET_COMMAND = 'set'
GET_COMMAND = 'get'
PING_COMMAND = 'ping'

COMMAND_LABEL = 'command'
COLLECTION_LABEL = 'collection'
OBJECT_NAME_LABEL = 'object'
SELECTOR_LABEL = 'selector'
DATA_LABEL = 'data'
RESULT_OF_LABEL = 'result_of'
SUCCESS_LABEL = 'success'


def construct_set(*, collection_name: Union[str, Associative],
                  object_name: Union[str, Associative],
                  selector: str = "", **kwargs) -> Object:
    command = {
        COMMAND_LABEL: SET_COMMAND,
        COLLECTION_LABEL: collection_name,
        OBJECT_NAME_LABEL: object_name,
        **kwargs
    }
    if selector != "":
        command[SELECTOR_LABEL] = selector
    return command


def construct_get(*, collection_name: Union[str, Associative],
                  object_name: Union[str, Associative],
                  selector: str = "", **kwargs) -> Object:
    command = {
        COMMAND_LABEL: GET_COMMAND,
        COLLECTION_LABEL: collection_name,
        OBJECT_NAME_LABEL: object_name,
        **kwargs
    }
    if selector != "":
        command[SELECTOR_LABEL] = selector
    return command


def construct_ping(**kwargs) -> Object:
    command = {
        COMMAND_LABEL: PING_COMMAND,
        **kwargs
    }
    return command
