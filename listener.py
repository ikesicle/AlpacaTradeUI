"""
Title: Alpaca Trade Ui
Writers: Ike Yang and Nikhil Gante

A user interface for viewing automated trading progress on the Alpaca API.

# NOTE: The API limits call amounts to 200 per minute.
# Any calls after this point will return 404 errors.

Structure:
Uses websockets to listen to stock changes and provide updates to client
Uses standard HTTP to perform portfolio actions
Object-based framework for "Algos"; each algo is an object which the client evaluates upon events and "asks" for what to do
"""

import asyncio
import websockets as ws
import alpaca_trade_api as alpaca
import datetime
import math
import os

print("Imports finished - Listener")

class AlpacaProfile(object):
  def __init__(self):
    self.alpacaConnection = 
    self.account = 
  

class Listener(object):
  baseurl = os.environ['APCA_API_BASE_URL']
  def __init__(self):
"""


