
def add_role(user_role: str):
    def defining_role(user):
        def wrapper(*args, **kwargs):
            new_user = user(*args, **kwargs)
            new_user.role = user_role
            return new_user
        return wrapper
    return defining_role


@add_role("employee")
class User:

    def __init__(self, name: str) -> None:
        self.name = name

    def login(self) -> None:
        print(f"You've been logged in {self.name}")


user = User("Josh")
print(user.role)