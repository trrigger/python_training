class Contact:

    def __init__(self, firstname=None, lastname=None, title=None, company=None, mobile=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.company = company
        self.mobile = mobile
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname