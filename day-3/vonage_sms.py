import vonage
from decouple import config
client = vonage.Client(key=config("CLIENT_KEY"), secret=config("CLIENT_SECRET"))
sms = vonage.Sms(client)

def get_message():
        s_from = input("Where is the message from? ")
        p_num = input("Where is the phone number to send? ")
        message = input("Where is the message? ")

        if p_num  == "" or message == "" or s_from == "":
            print("All fields are requiired")
            return
        return [s_from, p_num, message]

class VonAge():
    def __init__(self, sms_from, sms_to, message):
        self.sms_from = sms_from
        self.sms_to = sms_to
        self.message = message

    def send_vonage_message(self):
            responseData = sms.send_message(
                {
                    "from": f"{self.sms_from}",
                    "to": f"{self.sms_to}",
                    "text": f"{self.message}",
                }
            )

            if responseData["messages"][0]["status"] == "0":
                print("Message sent successfully.")
            else:
                print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

if __name__ == "__main__":
    sms_from, sms_to, message = get_message()
    vonage_sms = VonAge(sms_from, sms_to, message)
    vonage_sms.send_vonage_message()