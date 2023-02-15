from cli_entity.base import CLIEntity, CLICategory

class Folder(CLIEntity):
    def __init__(self, name, content=None):

        _value = content or []

        if not isinstance(_value, list):
            raise TypeError("Folder content is not a list!")

        super().__init__(
            name=name,
            category=CLICategory.FOLDER,
            value=_value
        )

    @property
    def content(self):
        return self.value

    def add_element(self, element):

        if not isinstance(element, CLIEntity):
            raise TypeError("Element is not a CLIEntity!")

        self.value.append(element)
