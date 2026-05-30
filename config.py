import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID", 0))

LOKI_URL = os.getenv("LOKI_URL")

SURICATA_LOG = os.getenv(
    "SURICATA_LOG",
    "/var/log/suricata/eve.json"
)

ADMIN_ROLE = os.getenv(
    "ADMIN_ROLE",
    "SOC Admin"
)
