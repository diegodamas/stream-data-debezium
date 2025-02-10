import faker
import psycopg2
import random
from datetime import datetime

fake = faker.Faker()


def generate_transaction() -> dict:

    user = fake.simple_profile()

    return {
        "transactionId": fake.uuid4(),
        "userId": user['username'],
        "timestamp": datetime.now().timestamp(),
        "amount": round(random.uniform(10, 1000)),
        "currency": random.choice(['USD', 'GBP']),
        'city': fake.city(),
        "country": fake.country(),
        "merchantName": fake.company(),
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'online_transaction']),
        "ipAddress": fake.ipv4(),
        "voucherCode": random.choice(['', 'DISCOUNT10', '']),
        "affiliateId": fake.uuid4()
    }


def create_table(conn: psycopg2.extensions.connection) -> None:

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id VARCHAR(255) PRIMARY KEY,
            user_id VARCHAR(255),
            timestamp TIMESTAMP,
            amount DECIMAL,
            currency VARCHAR (255),
            city VARCHAR (255),
            country VARCHAR (255),
            merchant_name VARCHAR (255),
            payment_method VARCHAR(255),
            ip_address VARCHAR (255),
            voucher_code VARCHAR(255),
            affiliate_id VARCHAR(255)
        )
        """)

    cursor.close()
    conn.commit()


if __name__ == "__main__":

    conn = psycopg2.connect(
        host='localhost',
        database='financial_db',
        user='postgres',
        password='postgres',
        port=5432
    )

    create_table(conn)
    transaction = generate_transaction()
    print(transaction)

    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO transactions (transaction_id, user_id, timestamp, amount, currency, city, country, merchant_name,
        payment_method, ip_address, affiliate_id, voucher_code)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (transaction["transactionId"],
                                                          transaction["userId"],
                                                          datetime.fromtimestamp(transaction["timestamp"]).strftime('%Y-%m-%d %H:%M:%S'),
                                                          transaction["amount"],
                                                          transaction["currency"],
                                                          transaction["city"],
                                                          transaction["country"],
                                                          transaction["merchantName"],
                                                          transaction["paymentMethod"],
                                                          transaction["ipAddress"],
                                                          transaction["affiliateId"],
                                                          transaction["voucherCode"])
    )

    cursor.close()
    conn.commit()
