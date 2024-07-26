import bcrypt


class PasswordHasher:

    def set_password(self, raw_password):
        raw_password_bytes = raw_password.encode('utf-8')
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(raw_password_bytes, salt).decode('utf-8')

    def check_password(self, raw_password):
        raw_password_bytes = raw_password.encode('utf-8')
        return bcrypt.checkpw(
            raw_password_bytes,
            self.password.encode('utf-8'))
