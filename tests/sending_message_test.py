import time

from tests import Authorization


class TestSendingMessage(Authorization):
    MESSAGE_TEXT = 'test message'

    def test_send_message_success(self):
        time.sleep(15)
        self.log_in()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('l_msg').click()
        dialog_list = self.driver.find_element_by_id('im_dialogs')
        dialog_list.find_elements_by_tag_name('li')[0].click()
        self.driver.find_element_by_id('im_editable0').send_keys(self.MESSAGE_TEXT)
        self.driver.find_element_by_class_name('im-send-btn_send').click()
        self.driver.find_element_by_class_name('im-page--back').click()
        user = dialog_list.find_elements_by_tag_name('li')[0]
        sending_message_text = user.find_element_by_class_name('nim-dialog--preview').text
        assert sending_message_text == self.MESSAGE_TEXT
