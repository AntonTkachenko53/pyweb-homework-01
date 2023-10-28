from abc import ABC, abstractmethod


class MessagePrinter(ABC):

    @abstractmethod
    def print_message(self):
        pass


class MessagePhoneError(MessagePrinter):

    def __init__(self, *args):
        self.message = 'Incorrect phone number format! Please provide correct phone number format.'

    def print_message(self):
        print(self.message)


class MessageBirthdayError(MessagePrinter):

    def __init__(self, *args):
        self.message = 'Incorrect date! Please provide correct date format.'

    def print_message(self):
        print(self.message)


class MessageEmailError(MessagePrinter):

    def __init__(self, *args):
        self.message = 'Incorrect email! Please provide correct email.'

    def print_message(self):
        print(self.message)


class MessageStatusError(MessagePrinter):

    def __init__(self, *args):
        self.message = 'There is no such status!'

    def print_message(self):
        print(self.message)


class MessageActionSearch(MessagePrinter):

    def __init__(self, *args):
        self.message = "There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote"

    def print_message(self):
        print(self.message)


class MessageCommandError(MessagePrinter):

    def __init__(self, *args):
        self.message = "There is no such command!"

    def print_message(self):
        print(self.message)


class MessageFindNameError(MessagePrinter):

    def __init__(self, *args):
        self.message = 'There is no such contact in address book!'

    def print_message(self):
        print(self.message)


class MessageParameterError(MessagePrinter):

    def __init__(self, *args):
        self.message = 'Incorrect parameter! Please provide correct parameter'

    def print_message(self):
        print(self.message)


class MessageGreeting(MessagePrinter):

    def __init__(self, *args):
        self.message = 'Hello. I am your contact-assistant. What should I do with your contacts?'

    def print_message(self):
        print(self.message)


class MessageTakenPrinter(MessagePrinter):

    def __init__(self, message):
        self.message = message

    def print_message(self):
        print(self.message)


class MessageFactory:
    def __init__(self):
        self.message_classes = {
            'PhoneError': MessagePhoneError,
            'BirthdayError': MessageBirthdayError,
            'EmailError': MessageEmailError,
            'StatusError': MessageStatusError,
            'ActionSearch': MessageActionSearch,
            'CommandError': MessageCommandError,
            'FindNameError': MessageFindNameError,
            'ParameterError': MessageParameterError,
            'Greeting': MessageGreeting,
        }

    def get_message(self, message_type):
        if message_type in self.message_classes:
            message_class = self.message_classes[message_type]()
            message_class.print_message()
        else:
            MessageTakenPrinter(message_type).print_message()
