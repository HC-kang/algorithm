from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket:

    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        # 초기화
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, key: Any, value: Any, stat: Status) -> None:
        # 모든 필드에서 값 설정
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        self.stat = stat


class OpenHash:

    def __init__(self, capacity: int) -> None:
        # 초기화
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> int:
        # 해시값 구하기
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)

    def rehash_value(self, key: Any) -> int:
        return(self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None
    
    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            return False
        
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False
    
    def remove(self, key: Any) -> int:
        p = self.search_node(key)
        if p is None:
            return False
            p.set_status(Status.DELETED)
            return True
    
    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i:2}', end = '')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('--미등록--')
            elif self.table[i].stat == Status.DELETED:
                print('--삭제 완료--')
