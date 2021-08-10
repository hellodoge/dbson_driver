from typing import Union, List, Dict

Object = Union[int, float, str,
               List['Object'],
               Dict[str, 'Object'],
               bool, None]

Array = List[Object]
Associative = Dict[str, Object]
