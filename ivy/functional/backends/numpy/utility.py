# global
import numpy as np
import numpy.array_api as npa
from typing import Union, Tuple, Optional, List


# noinspection PyShadowingBuiltins
def all(x: np.ndarray,
        axis: Optional[Union[int, Tuple[int], List[int]]] = None,
        keepdims: bool = False,
        out: Optional[np.ndarray]=None)\
        -> np.ndarray:
    return np.asarray(np.all(x, axis=axis, keepdims=keepdims, out=out))


# noinspection PyShadowingBuiltins
def any(x: np.ndarray,
        axis: Optional[Union[int, Tuple[int], List[int]]] = None,
        keepdims: bool = False)\
        -> np.ndarray:
    return np.asarray(npa.any(npa.asarray(x), axis=axis, keepdims=keepdims))
