from flask import Flask, flash, redirect, request, render_template
from models.contact import Contact

Contact.load_db()

# ========================================================
# Flask App
# ========================================================+
app = Flask(__name__)

app.secret_key = b'contact.app'

@app.route('/', methods=['GET'])
def index():
  return redirect('/contacts', 301)

@app.route('/contacts', methods=['GET'])
def contacts():
  search = request.args.get('q')
  if search is not None:
    contacts_set = Contact.search(search)
  else:
    contacts_set = Contact.all()
  return render_template("contacts_list.html", contacts=contacts_set)

@app.route('/contacts/add', methods=['GET'])
def contact_add_get():
  return render_template("contact_add.html", contact=Contact())

@app.route('/contacts/add', methods=['POST'])
def contact_add_post():
  contact = Contact(
    None,
    request.form['first_name'],
    request.form['last_name'],
    request.form['phone'],
    request.form['email']
  )
  if contact.save():
    flash("Contact added!")
    return redirect('/contacts')
  else:
    return render_template("contact_add.html", contact=contact)

if __name__ == "__main__":
  # For development convenience; in production use a WSGI server.
  app.run(debug=True)
