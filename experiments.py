import random
import string

def generate_unique_emails(count=3000):
    emails = set()
    while len(emails) < count:
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = f"{username}@test.test"
        emails.add(email)
    return emails

emails = generate_unique_emails()

with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Файл emails.txt с 3000 уникальными email создан.")
