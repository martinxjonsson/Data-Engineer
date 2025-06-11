import pandas as pd
import numpy as np

from faker import Faker # type: ignore

# Create a Faker instance
fake = Faker()

# Generate fake data
name = fake.name()
address = fake.address()
email = fake.email()

# Print the fake data
print(f"Name: {name}")
print(f"Address: {address}")
print(f"Email: {email}")