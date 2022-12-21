import check

import asyncio
import aiohttp
from typing import List
from os import system

from itertools import product
from string import ascii_lowercase


if __name__ == '__main__':
    # Ask user for what names to check
    usernames = input('Enter usernames to check (separate with commas): ').split(',')
    suffixLength = int(input("Enter suffix length: "))
    # Add suffixes to each username
    usernamesWithSuffixes = []
    allCombinations = [''.join(i) for i in product(ascii_lowercase, repeat = suffixLength)]
    for username in usernames:
        for x in allCombinations:
            usernamesWithSuffixes.append(username + x)
            print ("Adding " + username + x + " to list...")

    checker = check.Checker(usernamesWithSuffixes)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(checker.start())