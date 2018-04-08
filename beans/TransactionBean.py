class Transaction:
    def __init__(self, payload):
        self.order_number = payload[0]
        self.user_id = payload[1]
        self.game_id = payload[2]
        self.status = payload[3]
        self.total = payload[4]

    def to_dictionary(self):
        return {
            'order_number': self.order_number,
            'user_id': self.user_id,
            'game_id': self.game_id,
            'status': self.status,
            'total': self.total
        }
