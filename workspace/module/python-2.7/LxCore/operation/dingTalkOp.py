# coding=utf-8
# from dingtalkchatbot import chatbot


#
class DingTalkRobotMethod(object):
    def __init__(self, message):
        self._url = "https://oapi.dingtalk.com/robot/send?access_token=26cb8d095464fd3735eeac877975f673efe9befef8bdf118cceaa7f1ae74f5c3"
        self._datum = message
    #
    def _getUrl(self):
        pass
    #
    def send(self):
        pass
        # robot = chatbot.DingtalkChatbot(self._url)
        # robot.send_text(msg=self._datum)
