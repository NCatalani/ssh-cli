from cli_entity.folder import Folder
from cli_entity.connection import Connection

if __name__ == "__main__":


    connection = Connection(
        name="Oracle VM 1",
        username="opc",
        host="168.138.145.34",
        key_file="~/.ssh/id_rsa_oci"
    )

    folder = Folder(name="First Folder", content=[connection])

    print(folder)
