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
        return (f"Name: {self.value}")

class Phone(Field):
    def __init__(self, phone):
        if not self.validate_phone(phone):
            raise ValueError("Невірний формат номеру телефону")
        super().__init__(phone)

    def validate_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()

    def __str__(self):
        return (f"Phone: {self.phone}")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        found = False
        for p in self.phones:
            if p.value == old_phone:
                found = True
                if p.validate_phone(new_phone):
                    p.value = new_phone
                else:
                    raise ValueError("Новий номер телефону невалідний")
        if not found:
            raise ValueError("Такого номеру телефону не існує")
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            return self.data.pop(name)
