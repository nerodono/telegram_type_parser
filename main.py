from telegram_type_parser import parse

tps = ["Array of Array of Integer", "Array of Array of Composite", "Integer", "String"]

for tp in tps:
    print(tp, "=", parse(tp))
