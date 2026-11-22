orders_example = [
    {"order_id": 1, "amount": 1200},
    {"order_id": 2, "amount": 800},
    {"order_id": 3, "amount": 1500},
    {"order_id": 4, "amount": 450},
    {"order_id": 5, "amount": 3200},
    {"order_id": 6, "amount": 950},
    {"order_id": 7, "amount": 2100},
    {"order_id": 8, "amount": 1750},
    {"order_id": 9, "amount": 600},
    {"order_id": 10, "amount": 4800},
]


def calculate_average_order_value(orders):
    if not orders:
        print("Nothing to count")
        return 0

    total = sum(order["amount"] for order in orders)
    average = total / len(orders)

    print(f"For {len(orders)} orders average is {average}")
    return average


if __name__ == "__main__":
    calculate_average_order_value(orders_example)
