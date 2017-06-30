from model.contact import Contact
import random
import string

constant = [
    Contact(firstname='firstname1', lastname='lastname1', title='title1', company='company1', mobilephone='mobile1', email='test@mail_1.ru'),
    Contact(firstname='firstname2', lastname='lastname2', title='title2', company='company2', mobilephone='mobile2', email='test@mail_2.ru'),
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname='', lastname='', title='', company='', mobilephone='', email='test@mail.ru')] + [
        Contact(firstname=random_string('firstname', 10), lastname=random_string('Petrov', 10), title=random_string('engeneer', 20),
                company=random_string('top labs', 20), mobilephone=random_string('8-888-888-88-88', 30),
                email=random_string('test@mail.ru', 30))
for i in range(5)
    ]