from enum import Enum
from http.client import PROCESSING

class AprovedStatusEnum(Enum):
    PROCESSING = 0
    APROVED = 1
    REJECTED = 2
