from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import uuid4
from typing import *
import time
from json import dumps


@dataclass
class BaseEntity(ABC):
    id: int
    created_at: int
    updated_at: int
    uuid: str

    def save(self):
        if self.created_at is None:
            self.uuid = str(uuid4())
            self.created_at = int(time.time() * 1000)
        else:
            self.updated_at = int(time.time() * 1000)
        values = self.get_values()
        values['id'] = self.id
        values['created_at'] = self.created_at
        values['updated_at'] = self.updated_at
        values['uuid'] = self.uuid

        print(dumps(values))

    @abstractmethod
    def get_values(self) -> Dict[str, object]:
        pass


@dataclass
class User(BaseEntity):
    email: str

    def get_values(self) -> Dict[str, object]:
        return {
            'email': self.email
        }


if __name__ == '__main__':
    user = User(1, None, None, None, 'example@domain.com')
    print(user)
    user.save()
    user.save()
    time.sleep(1)
    user.save()