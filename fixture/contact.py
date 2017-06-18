from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_creating_form(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/edit.php')):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_creating_form()
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/index.php')):
            wd.get("http://localhost/addressbook/index.php")
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_css_selector("input[onclick*='DeleteSel()").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_first(self, contact):
        wd = self.app.wd
        if not (wd.current_url.endswith('/index.php')):
            wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def modify_first(self, new_contact_data):
        wd = self.app.wd
        if not (wd.current_url.endswith('/index.php')):
            wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/index.php')):
            wd.get("http://localhost/addressbook/index.php")
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            wd.get("http://localhost/addressbook/index.php")
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                columns = element.find_elements_by_tag_name('td')
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=columns[2].text, lastname=columns[1].text, id=id))
        return list(self.contact_cache)
