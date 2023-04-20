from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time
import psutil

from settings import dev


class Interview_Questions(object):
    def __init__(self):
        self.title_1 = dev.TITLE_1
        self.title_2 = dev.TITLE_2
        self.title_3 = dev.TITLE_3
        self.title_4 = dev.TITLE_4
        self.type_keys = dev.TYPE_KEYS
        self.send_keys = dev.SEND_KEYS
        self.we_chat_id = dev.WE_CHAT_ID
        self.backend_uia = dev.BACKEND_UIA
        self.we_chat_path = dev.WE_CHAT_PATH
        self.class_name = dev.CLASS_NAME
        self.control_type_1 = dev.CONTROL_TYPE_1
        self.control_type_2 = dev.CONTROL_TYPE_2

    def get_pid(self, we_chat_id):
        """输入进程名，获取PID"""
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            if we_chat_id in p.name():
                return pid

    def awaken(self):
        """微信挂在后台时，通过再次运行唤醒"""
        # 获取微信PID并获取微信窗口
        we_chat_id = self.get_pid(self.we_chat_id)
        app = Application(backend=self.backend_uia).connect(process=we_chat_id)
        we_chat_main_dialog = app.window(class_name=self.class_name)
        # 微信挂在后台时，通过再次运行唤醒
        if not we_chat_main_dialog.exists():
            Application().start(self.we_chat_path)
        return we_chat_main_dialog

    def search(self, chat_name):
        # 通过搜索，定位聊天
        we_chat_main_dialog = self.awaken()
        # 通过先最小化，再恢复使得窗口置顶
        we_chat_main_dialog.minimize()
        we_chat_main_dialog.restore()
        search_elem = we_chat_main_dialog.child_window(control_type=self.control_type_1, title=self.title_1)
        search_elem.click_input()
        search_elem.type_keys(self.type_keys).type_keys(chat_name)
        time.sleep(1)
        send_keys(self.send_keys)

    def send_message(self, chat_name):
        """点击要发送消息的聊天"""
        we_chat_main_dialog = self.awaken()
        chat_list = we_chat_main_dialog.child_window(control_type=self.control_type_2, title=self.title_2)
        for chat_item in chat_list.items():
            if chat_name in chat_item.element_info.name:
                chat_item.click_input()
                time.sleep(1)

    def get_message(self):
        """获取聊天记录"""
        we_chat_main_dialog = self.awaken()
        message_list = we_chat_main_dialog.child_window(control_type=self.control_type_2, title=self.title_4)
        for message_item in message_list.items():
            print(message_item)

    def input_send(self, message):
        """输入并发送消息"""
        we_chat_main_dialog = self.awaken()
        edit_elem = we_chat_main_dialog.child_window(control_type=self.control_type_1, title=self.title_3)
        edit_elem.type_keys(self.type_keys).type_keys(message, with_spaces=True)
        time.sleep(1)
        send_keys(self.send_keys)

    def send(self):
        """
        chat_name 需要发送消息的聊天名称
        message  需要发送的消息
        :return:
        """
        chat_name = dev.CHAT_NAME
        message = dev.MESSAGE
        self.search(chat_name)
        self.send_message(chat_name)
        self.input_send(message)
        self.get_message()


Interview_Questions()