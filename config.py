# AsmSafone
# Radio Player
# Join @disneygrou

import os
from os import environ

class Config:
  API_ID = int(environ["API_ID"])
  API_HASH = environ["API_HASH"]
  SESSION = environ["SESSION"]
  CHAT_NAME = environ["CHAT_NAME"]
  ADMIN = int(environ["ADMIN"])
