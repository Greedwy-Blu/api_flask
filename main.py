from flask import Flask
from src.server.instance import server
from src.controllers.book import *


server.run()

