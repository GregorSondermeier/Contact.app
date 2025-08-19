import json

# ========================================================
# Contact Model
# ========================================================
PAGE_SIZE = 100

class Contact:
    # mock contacts database
    db = {}

    def __init__(self, id_=None, first_name=None, last_name=None, phone=None, email=None):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.errors = {}

    @classmethod
    def load_db(cls):
        with open('db/contacts.json', 'r') as contacts_file:
            contacts = json.load(contacts_file)
            cls.db.clear()
            for contact in contacts:
                cls.db[contact['id']] = Contact(contact['id'], contact['first_name'], contact['last_name'], contact['phone'], contact['email'])

    @classmethod
    def all(cls, page=1):
        page = int(page)
        start = (page - 1) * PAGE_SIZE
        end = start + PAGE_SIZE
        return list(cls.db.values())[start:end]

    @classmethod
    def search(cls, text):
        result = []
        for c in cls.db.values():
            match_first = c.first_name is not None and text in c.first_name
            match_last = c.last_name is not None and text in c.last_name
            match_email = c.email is not None and text in c.email
            match_phone = c.phone is not None and text in c.phone
            if match_first or match_last or match_email or match_phone:
                result.append(c)
        return result