is_hot = True
is_cold = True

if is_hot:
    print("Warmer Tag heute")
    print("Trink Wasser")
elif is_cold:
    print("Kalter Tag heute")
    print("Zieh dich warm an")
else:
    print("Schönes Wetter heute")

credit = False
price = 100000

if credit:
    payment = price * 0.1
else:
    payment = price * 0.2
print(f"down payment: ${int(payment)}")