import random
import string
from schemas.otp import OTPUse, OTPCreate, OTPRead


class OTPManager(object):
    def __init__(self):
        self.active_keys: dict[str, OTPRead] = {}

    def generate_otp(self, template: OTPCreate) -> OTPRead:
        otp_secret: str = ""
        for index in range(template.key_length):
            otp_secret += random.SystemRandom().choice(string.ascii_uppercase + string.digits)
        otp : OTPRead = OTPRead(name=template.name,secret=otp_secret)
        self.active_keys[otp_secret] = otp
        return otp

    def get_list(self) -> list[OTPRead]:
        return list(self.active_keys.values())

    def remove_otp(self, otp: OTPUse):
        self.active_keys.pop(otp.secret, None)

    def clear_active_keys(self):
        self.active_keys: dict[str, str] = {}

    def verify_otp(self, otp: OTPUse) -> bool:
        return otp.secret in self.active_keys.keys()

    def consume_otp(self, otp: OTPUse) -> OTPRead:
        if not self.verify_otp(otp):
            raise Exception("OTP does not exist.")
        otp_read: OTPRead = self.active_keys[otp.secret]
        self.remove_otp(otp)
        return otp_read

manager = OTPManager()

if __name__ == '__main__':
    manager.generate_otp(OTPCreate(name="Test"))
    print(manager.active_keys)

