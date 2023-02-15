import subprocess

from cli_entity.base import CLIEntity, CLICategory


class Connection(CLIEntity):
    def __init__(self, name, username, host, password=None, key_file=None):
        super().__init__(
            name=name,
            category=CLICategory.CONNECTION,
            value={}
        )

        self.username = username
        self.host = host
        self.password = password
        self.key_file = key_file

    @property
    def username(self):
        return self.value["username"]

    @property
    def host(self):
        return self.value["host"]

    @property
    def password(self):
        return self.value["password"]

    @property
    def key_file(self):
        return self.value["key_file"]

    @username.setter
    def username(self, username):
        if not isinstance(username, str):
            raise TypeError("Username is not a str")

        self.value["username"] = username

    @host.setter
    def host(self, host):
        if not isinstance(host, str):
            raise TypeError("Host is not a str")

        self.value["host"] = host

    @password.setter
    def password(self, password):
        if password is not None and not isinstance(password, str):
            raise TypeError("Password is not a str")

        self.value["password"] = password

    @key_file.setter
    def key_file(self, key_file):
        if key_file is not None and not isinstance(key_file, str):
            raise TypeError("Key_file is not a str")

        self.value["key_file"] = key_file

    def __generate_login_command(self) -> list[str]:

        command: list = ["ssh"]

        if self.key_file is not None:
            command.append("-i")
            command.append(f"{self.key_file}")

        command.append(f"{self.username}@{self.host}")

        return command

    def login(self) -> None:

        cmd = self.__generate_login_command()

        subprocess.run(
            cmd
        )
