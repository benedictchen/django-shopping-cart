import string, random
from .models import Order


class OrderIdGenerator:

    id_generator_size = 6

    id_generator_attempts = 0

    @classmethod
    def generate_order_id(cls, size=6, chars=string.ascii_uppercase + string.digits):
        """
        Generates a unique identifier for a particular order.
        :param size: Number. The length of the unique identifier. Defaults to six chars.
        :param chars: String. The types of characters used in the generation of the id.
        :return: String. The unique identifier generated.
        """
        order_id = ''.join(random.choice(chars) for _ in range(size))
        try:
            existing = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            return order_id
        # if no exception, then get a new id.
        cls.id_generator_attempts += 1
        if cls.id_generator_attempts > 5:
            cls.id_generator_size += 1
        return cls.generate_order_id(cls.id_generator_size)

