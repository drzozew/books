def send_messages(messages, sent_messages1):
    while messages:
        sent_messages = messages.pop(0)
        sent_messages1.append(sent_messages)


messages = ['jaka', 'woda', 'mleko']
sent_messages1 = []

print("Lista zakupów:")
for x in messages:
    print(f"  {x}")
send_messages(messages[:], sent_messages1)

print("Zrobione zakupy: ")
for x in sent_messages1:
    print(f"  {x}")

print(messages)
print(sent_messages1)
