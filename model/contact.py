from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None,
                 title=None, company=None,
                 homephone=None, workphone=None,
                 mobilephone=None, secondaryphone=None,
                 email=None, email_2=None, email_3=None,
                 id=None, address=None,
                 all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.company = company
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.address = address
        self.id = id

    def __repr__(self):
        return "%s:%s:%s;%s;%s;%s;%s" % (self.id, self.firstname, self.lastname, self.title, self.company, self.mobilephone, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
