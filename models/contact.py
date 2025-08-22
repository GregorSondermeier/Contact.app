import json
import uuid

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

  def validate(self):
    if not self.email:
      self.errors['email'] = "Email Required"
    existing_contact = next(filter(lambda c: c.id != self.id and c.email == self.email, Contact.db.values()), None)
    if existing_contact:
      self.errors['email'] = "Email Must Be Unique"
    return len(self.errors) == 0

  def save(self):
    if not self.validate():
      return False
    if self.id is None:
      self.id = str(uuid.uuid4())
      Contact.db[self.id] = self
    Contact.save_db()
    return True

  @classmethod
  def load_db(cls):
    with open('db/contacts.json', 'r') as contacts_file:
      contacts = json.load(contacts_file)
      cls.db.clear()
      for contact in contacts:
        cls.db[contact['id']] = Contact(contact['id'], contact['first_name'], contact['last_name'], contact['phone'], contact['email'])

  @staticmethod
  def save_db():
    out_arr = [c.__dict__ for c in Contact.db.values()]
    with open("db/contacts.json", "w") as f:
      json.dump(out_arr, f, indent=2)

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
