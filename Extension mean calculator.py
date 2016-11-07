print("This is a mean calculator XD")
print("▓       ▓       ▓ ▓▓▓▓▓▓▓  ▓      ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓ ▓       ▓ ▓▓▓▓▓▓▓")
print(" ▓     ▓ ▓     ▓  ▓        ▓      ▓       ▓     ▓ ▓▓     ▓▓ ▓      ")
print("  ▓   ▓   ▓   ▓   ▓▓▓▓▓▓▓  ▓      ▓       ▓     ▓ ▓ ▓   ▓ ▓ ▓▓▓▓▓▓▓")
print("   ▓ ▓     ▓ ▓    ▓        ▓      ▓       ▓     ▓ ▓  ▓ ▓  ▓ ▓      ")
print("    ▓       ▓     ▓▓▓▓▓▓▓  ▓▓▓▓▓▓ ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓ ▓   ▓   ▓ ▓▓▓▓▓▓▓")
print("\nType it in this format:    mean([number1,number2,number3,...])")
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
