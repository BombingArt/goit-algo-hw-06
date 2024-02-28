from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"Name: {self.value}"

class Phone:
    def __init__(self, phone):
        self.phone = self.validate_phone(phone)

    def validate_phone(self, phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Номер має складатись з 10 цифр")
        return phone

    def __str__(self):
        return f"Phone: {self.phone}"

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        phone_found = False
        for p in self.phones:
            if p.phone == old_phone:
                if not new_phone.isdigit() or len(new_phone) != 10:
                    raise ValueError("Новий номер має складатись з 10 цифр")
                p.phone = new_phone
                phone_found = True
                break
        if not phone_found:
            raise ValueError("Номер не знайдено в записі")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.phone for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError("Запис з таким ім'ям вже існує")
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            return self.data.pop(name)
        else:
            raise ValueError("Запис з таким ім'ям не знайдено")
