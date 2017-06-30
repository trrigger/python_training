from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname='', lastname='', title='', company='', mobilephone='', email='test@mail.ru')] + [
        Contact(firstname=random_string('firstname', 10), lastname=random_string('Petrov', 10), title=random_string('engeneer', 20),
                company=random_string('top labs', 20), mobilephone=random_string('8-888-888-88-88', 30),
                email=random_string('test@mail.ru', 30))
for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, 'w') as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.encode(file)