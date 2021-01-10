import time
from tests import Authorization


class TestSearchAndInvite(Authorization):
    def test_search_user(self):
        self.driver.implicitly_wait(10)
        self.log_in()
        self.driver.find_element_by_id('l_fr').click()
        self.driver.find_element_by_id('invite_button').click()
        users = self.driver.find_elements_by_class_name('friends_find_user')
        invite_btn = users[0].find_elements_by_class_name('friends_find_user_add')[0]
        invite_btn.click()
        time.sleep(2)
        assert not invite_btn
