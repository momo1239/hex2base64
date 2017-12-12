import base64
import binascii

print("Enter the Hex Digit...")

bait = binascii.unhexlify(input())
data = base64.b64encode(bait)

bata = str(data)

print(bata + "Is the base64string")


