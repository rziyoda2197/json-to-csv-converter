class User:
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role
        self.permissions = []

class Role:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.permissions = []

class Permission:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class UserPermissionSystem:
    def __init__(self):
        self.users = []
        self.roles = []
        self.permissions = []

    def add_user(self, id, username, role_id):
        user = User(id, username, self.get_role(role_id))
        self.users.append(user)

    def add_role(self, id, name):
        role = Role(id, name)
        self.roles.append(role)

    def add_permission(self, id, name):
        permission = Permission(id, name)
        self.permissions.append(permission)

    def assign_permission(self, user_id, permission_id):
        user = self.get_user(user_id)
        permission = self.get_permission(permission_id)
        if user and permission:
            user.permissions.append(permission)

    def get_user(self, id):
        for user in self.users:
            if user.id == id:
                return user
        return None

    def get_role(self, id):
        for role in self.roles:
            if role.id == id:
                return role
        return None

    def get_permission(self, id):
        for permission in self.permissions:
            if permission.id == id:
                return permission
        return None

    def check_permission(self, user_id, permission_id):
        user = self.get_user(user_id)
        permission = self.get_permission(permission_id)
        if user and permission:
            return permission in user.permissions
        return False

# Misol
system = UserPermissionSystem()

system.add_role(1, "Admin")
system.add_role(2, "Moderator")
system.add_role(3, "User")

system.add_permission(1, "Create Post")
system.add_permission(2, "Delete Post")
system.add_permission(3, "Comment Post")

system.add_user(1, "admin", 1)
system.add_user(2, "moderator", 2)
system.add_user(3, "user", 3)

system.assign_permission(1, 1)
system.assign_permission(1, 2)
system.assign_permission(2, 3)

print(system.check_permission(1, 1))  # True
print(system.check_permission(1, 2))  # True
print(system.check_permission(1, 3))  # False
print(system.check_permission(2, 3))  # True
print(system.check_permission(3, 3))  # True
