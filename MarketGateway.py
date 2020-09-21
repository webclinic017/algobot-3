# Market Gateway Class

import sys
import time
import traceback
import alpaca_trade_api as tradeapi
from kiteconnect import KiteConnect

class MarketGateway:

    def __init__(self):

        # get credentials from external txt file

        # alpaca live trading
        # alpaca_url = "https://api.alpaca.markets"
        # alpaca_key = "AKI0HM4U3MRV06543ENW"
        # alpaca_secret = "ARvZlbpIGYVGbNY5ZVIwDhjZIpTMYANJ5TzLKp2J"
        # self.alpaca = tradeapi.REST(alpaca_key,alpaca_secret,alpaca_url,'v2')

        # alpaca paper trading
        alpaca_url = "https://paper-api.alpaca.markets"
        alpaca_key = "PKMCXT8TUQH0YR06LFN7"
        alpaca_secret = "euc5bT52sNStFI4PDKg8hrQvrZxF/MeLQak6WEhi"
        self.alpaca = tradeapi.REST(alpaca_key,alpaca_secret,alpaca_url,'v2')

    # ------------------------------------------------
    # Gateway IN Functions
    # ------------------------------------------------

    # get market data
    def get_last_quote(self, symbol: str):
        return self.alpaca.get_last_quote(symbol)

    # get barset
    def get_barset(self,
                    symbols,
                    timeframe: str,
                    limit: int = None,
                    start: str = None,
                    end: str = None,
                    after: str = None,
                    until: str = None):
        return self.alpaca.get_barset(symbols,
                                        timeframe,
                                        limit,
                                        start,
                                        end,
                                        after,
                                        until)

    # Get the clock
    def get_clock(self):
        return self.alpaca.get_clock()

    # get account info
    def get_account(self):
        return self.alpaca.get_account()

    # List all orders
    def get_all_orders(self):
        return self.alpaca.list_orders()

    # Get a specific order via order_id
    def get_order(self, order):
        return self.alpaca.get_order(order[0])

    # List all Positions
    def get_all_positions(self):
        return self.alpaca.list_positions()

    # Get a specific position
    def get_position(self, symbol):
        return self.alpaca.get_position(symbol)

    # Get portfolio history
    def get_portfolio_history(self,start,end):
        return self.alpaca.get_portfolio_history(start,end)

    # ------------------------------------------------
    # Gateway OUT Functions
    # ------------------------------------------------

    # Close a position via it's position_id
    def close_position(self, symbol):
        return self.alpaca.close_position(symbol)

    # close all positions
    def close_all_positions(self):
        return self.alpaca.close_all_positions()

    # modify an order
        # add additional params based on # of order keys
    def modify_order(self, order):
        return self.alpaca.replace_order(order[0])

    # cancel an order via it's order_id
    def cancel_order(self, order):
        return self.alpaca.cancel_order(order[0])

    # cancel all orders
    def cancel_all_orders(self):
        return self.alpaca.cancel_all_orders()

    # Submit order
    def submit_order(self, order):
        return self.alpaca.submit_order(order[0], order[1], order[2], order[3], order[4])

# EOF
