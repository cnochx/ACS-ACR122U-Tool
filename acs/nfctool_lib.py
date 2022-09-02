"""
Python 3 ACS-ACR122U-Tool
"""
from smartcard.System import readers
from smartcard.utils import toHexString
from smartcard.Cardtype import AnyCardType

import sys

class Reader:

    def __int__(self):
        """create an ACR122U object
        doc available here: http://downloads.acs.com.hk/drivers/en/API-ACR122U-2.02.pdf"""

