from solana.rpc.api import Client
from solders.keypair import Keypair #type: ignore

PUB_KEY = ""
PRIV_KEY = ""
RPC = ""
client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)