Area=int(input("Enter a area="))
Internal=int(input("Enter a internal="))
External=int(input("Enter a external="))

IC=6*Area*Internal
EC=8*Area*External

Total= IC + EC

print(f"Interior wall {IC}")
print(f"Exterior wall {EC}")
print(f"Total is {Total}")
