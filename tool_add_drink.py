#!/usr/bin/env python
# coding=utf-8

import argparse

from database.storage import init_db
from database.storage import get_session
from database.models.drink import Drink

init_db()

parser = argparse.ArgumentParser(description='Adds new drinks to the drink database.')
parser.add_argument('--ean', required=True, help='The EAN code of the barcode')
parser.add_argument('--name', required=True, help='The name that should be displayed')
parser.add_argument('--size', required=True, type=float, help='The size of the bottle, eg. 0.33l or 0,5l, ommitting the "l"')

args = parser.parse_args()

session = get_session()
ev = Drink(
    args.ean,
    args.name,
    args.size
)

session.add(ev)
session.commit()