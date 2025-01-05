from abc import ABC


class Chat(ABC, abstract=True):

    def send_message(self, group_name, message):
        pass


