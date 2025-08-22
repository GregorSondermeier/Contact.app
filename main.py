from flask import Flask, flash, redirect, request, render_template
from models.contact import Contact

Contact.load_db()

# ========================================================
# Flask App
# ========================================================+
app = Flask(__name__)

@app.route('/')
def index():
  return redirect('/contacts', 301)

@app.route('/contacts')
def contacts():
  search = request.args.get('q')
  if search is not None:
    contacts_set = Contact.search(search)
  else:
    contacts_set = Contact.all()
  return render_template("contacts_list.html", contacts=contacts_set)

if __name__ == "__main__":
  # For development convenience; in production use a WSGI server.
  app.run(debug=True)
