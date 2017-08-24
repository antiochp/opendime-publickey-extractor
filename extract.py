import base64
import binascii
import json

from pprint import pprint

from bitcoin.core.key import CPubKey
from bitcoin.signmessage import BitcoinMessage

# TODO - read this file from a mounted OpenDime
with open('./variables_3.json') as data_file:
    data = json.load(data_file)

pprint(data)
pprint(data['va'])
parts = data['va'].split('|')
pprint(parts)

msg = parts[0]
sig = parts[2]

pprint(sig)
sig = sig+"==="
pprint(sig)
sig = base64.b64decode(sig, '-_')

msg = BitcoinMessage(msg)
hash = msg.GetHash()

pubkey = CPubKey.recover_compact(hash, sig)
pprint(pubkey)
hex_bytes = binascii.hexlify(pubkey)
pprint(hex_bytes)
hex_str = hex_bytes.decode("ascii")
pprint(hex_str)
