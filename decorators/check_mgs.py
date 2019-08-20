import time

def check_if_msg_can_be_sent(func):
    def validate(*args):
        if 8 <= time.localtime().tm_hour < 11:
            print("Message sent:")
            return  func(*args) #without return None will be returned to caller
        else:
            print("Out of Business hrs message not sent")
    return validate

@check_if_msg_can_be_sent
def send_msg(msg):
    print(f"\t{msg}")

#driver code
val = input("Enter message to send:")
send_msg(val)