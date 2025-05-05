from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    role: str  

class UserService:
    def __init__(self):
        self._users: List[User] = []

    def create(self, user_data: User) -> None:
        self._users.append(user_data)

    def list(self) -> List[User]:
        return self._users

    def get(self, user_id: int) -> Optional[User]:
        return next((u for u in self._users if u.id == user_id), None)

    def update(self, user_id: int, new_data: User) -> bool:
        for idx, u in enumerate(self._users):
            if u.id == user_id:
                self._users[idx] = new_data
                return True
        return False

    def delete(self, user_id: int) -> bool:
        u = self.get(user_id)
        if u:
            self._users.remove(u)
            return True
        return False
