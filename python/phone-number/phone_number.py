class PhoneNumber:
    def __init__(self, number):
        self.number = self.cleaner(number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[6:]

    def cleaner(self, number):
        clean = "".join([i for i in number if i.isdigit()])

        if len(clean) == 11 and clean[0] == '1':
            clean = clean[1:]
        if len(clean) != 10:
            raise ValueError("Invalid phone number")
        if clean[0] not in "23456789":
            raise ValueError("Invalid Area Code")
        if clean[3] not in "23456789":
            raise ValueError("Invalid Exchange Code")
        return clean

    def pretty(self):
        return (f"({self.area_code}) {self.exchange_code}-{self.subscriber_number}")
