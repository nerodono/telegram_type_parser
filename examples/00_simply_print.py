from telegram_type_parser import parse

tps = [
    "Array of Message",
    "Array of Array of Message",
    "Integer",
    "String",
    "Boolean",
]

for tp in tps:
    print(tp, "is", parse(tp))

# Expected output is:
# Array of Message is list[Message]
# Array of Array of Message is list[list[Message]]
# Integer is int
# String is str
# Boolean is bool
