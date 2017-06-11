class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_creating_form(self):
        wd = self.app.wd
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

    def delete_first_contact(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_css_selector("input[onclick*='DeleteSel()").click()
        wd.switch_to_alert().accept()

    def edit_first(self, contact):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def modify_first(self, new_contact_data):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

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
        wd.get("http://localhost/addressbook/index.php")
        return len(wd.find_elements_by_name("selected[]"))
