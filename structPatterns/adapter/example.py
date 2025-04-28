class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class DbAdapter:
    def insert_user(self, user):
        raise NotImplementedError

    def get_user_by_id(self, user_id):
        raise NotImplementedError

    def update_user(self, user):
        raise NotImplementedError

    def delete_user(self, user_id):
        raise NotImplementedError

class MysqlDbAdapter(DbAdapter):
    def insert_user(self, user):
        # mysql insert user code here
        print("insert user into mysql")

    def get_user_by_id(self, user_id):
        # mysql get user by id code here
        print("get user by id from mysql")
        # 假设从数据库获取用户信息
        return User(user_id, 'mysql_user', 'mysql_email')

    def update_user(self, user):
        # mysql update user code here
        print("update user in mysql")

    def delete_user(self, user_id):
        # mysql delete user code here
        print("delete user from mysql")

class PostgresqlDbAdapter(DbAdapter):
    def insert_user(self, user):
        # postgresql insert user code here
        print("insert user into postgresql")

    def get_user_by_id(self, user_id):
        # postgresql get user by id code here
        print("get user by id from postgresql")
        return User(user_id, 'postgresql_user', 'postgresql_email')

    def update_user(self, user):
        # postgresql update user code here
        print("update user in postgresql")

    def delete_user(self, user_id):
        # postgresql delete user code here
        print("delete user from postgresql")


class UserService:
    def __init__(self, db_adapter):
        self.db_adapter = db_adapter

    def create_user(self, name, email):
        try:
            user = User(None, name, email)
            self.db_adapter.insert_user(user)
            return user
        except Exception as e:
            print(f"Error creating user: {e}")
            return None

    def get_user_by_id(self, user_id):
        try:
            return self.db_adapter.get_user_by_id(user_id)
        except Exception as e:
            print(f"Error getting user by id: {e}")
            return None

    def update_user(self, user_id, name, email):
        try:
            user = User(user_id, name, email)
            self.db_adapter.update_user(user)
        except Exception as e:
            print(f"Error updating user: {e}")

    def delete_user(self, user_id):
        try:
            self.db_adapter.delete_user(user_id)
        except Exception as e:
            print(f"Error deleting user: {e}")


if __name__ == '__main__':
    mysql_db_adapter = MysqlDbAdapter()
    postgresql_db_adapter = PostgresqlDbAdapter()

    mysql_user_service = UserService(mysql_db_adapter)
    postgresql_user_service = UserService(postgresql_db_adapter)

    mysql_user_service.create_user("mysql_user", "mysql_email")
    postgresql_user_service.create_user("postgresql_user", "postgresql_email")

    mysql_user = mysql_user_service.get_user_by_id(1)
    postgresql_user = postgresql_user_service.get_user_by_id(1)

    mysql_user_service.update_user(1, "new_mysql_user", "new_mysql_email")
    postgresql_user_service.update_user(1, "new_postgresql_user", "new_postgresql_email")

    mysql_user_service.delete_user(1)
    postgresql_user_service.delete_user(1)
