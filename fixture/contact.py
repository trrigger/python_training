from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

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
        self.change_field_value("homephone", contact.homephone)
        self.change_field_value("workphone", contact.workphone)
        self.change_field_value("mobilephone", contact.mobilephone)
        self.change_field_value("secondaryphone", contact.secondaryphone)
        self.change_field_value("email", contact.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        if not (wd.current_url.endswith('/index.php')):
            self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_css_selector("input[onclick*='DeleteSel()").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_first(self):
        self.select_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        if not (wd.current_url.endswith('/index.php')):
            self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def modify_first(self, new_contact_data):
        wd = self.app.wd
        if not (wd.current_url.endswith('/index.php')):
            self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath('//*[@title="Edit"]').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath('//*[@title="Details"]').click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("homephone", contact.homephone)
        self.change_field_value("workphone", contact.workphone)
        self.change_field_value("mobilephone", contact.mobilephone)
        self.change_field_value("secondaryphone", contact.secondaryphone)
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
            self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                columns = element.find_elements_by_tag_name('td')
                firstname = columns[2].text
                lastname = columns[1].text
                id = columns[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = columns[5].text
                all_emails = columns[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        title = wd.find_element_by_name('title').get_attribute('value')
        company = wd.find_element_by_name('company').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email_2 = wd.find_element_by_name('email2').get_attribute('value')
        email_3 = wd.find_element_by_name('email3').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('text')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        secondaryphone = wd.find_element_by_name('phone2').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, title=title, company=company,
                       email=email, email_2=email_2, email_3=email_3, address=address,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)
