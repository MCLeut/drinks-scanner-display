#!/usr/bin/env python2
# coding=utf8
import logging
import os
import sys

sys.path.append(os.path.dirname(__file__)+"/../")
from users.users import Users

logging.basicConfig()

def main(args):
    for user in Users.get_all():
        user['meta']['last_emailed'] = 0
        user['meta']['last_drink_notification'] = 0
        Users.save(user)

if __name__ == "__main__":
    sys.exit(main(sys.argv))