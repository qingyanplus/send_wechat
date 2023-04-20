from utils import Input


CHAT_NAME = Input.input_chat('请输入要发送消息的人或群：')
MESSAGE = Input.input_message('请输入要发送的消息：')
WE_CHAT_PATH = r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"  # 微信路径  C:\Program Files (x86)\Tencent\WeChat
WE_CHAT_ID = 'WeChat.exe'   # 微信程序
BACKEND_UIA = 'uia'   #
CLASS_NAME = 'WeChatMainWndForPC'
TYPE_KEYS = '^a'
SEND_KEYS = '{ENTER}'
CONTROL_TYPE_1 = 'Edit'
CONTROL_TYPE_2 = 'List'
TITLE_1 = '搜索'
TITLE_2 = '会话'
TITLE_3 = '输入'
TITLE_4 = '消息'