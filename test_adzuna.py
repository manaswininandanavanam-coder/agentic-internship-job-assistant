import os
from pathlib import Path
from dotenv import dotenv_values, load_dotenv


BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

print("ENV FILE:")
print(ENV_PATH)

print("\nENV EXISTS:")
print(ENV_PATH.exists())


# Read .env directly
config = dotenv_values(ENV_PATH)

print("\nVARIABLE NAMES FOUND IN .env:")

for key in config.keys():
    print("-", key)


# Load variables
load_dotenv(ENV_PATH)

print("\nEXPECTED VARIABLES:")

print(
    "ADZUNA_APP_ID exists:",
    bool(os.getenv("ADZUNA_APP_ID"))
)

print(
    "ADZUNA_APP_KEY exists:",
    bool(os.getenv("ADZUNA_APP_KEY"))
)