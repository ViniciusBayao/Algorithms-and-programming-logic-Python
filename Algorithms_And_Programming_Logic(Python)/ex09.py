"""
Make an algorithm that reads how much money a person has in their wallet (in BRL)
and show how many dollars the person can buy. Consider US$1.00 = R$3.45.
"""
brl = float(input("Type how much BRL you have in your wallet: "))
dollar = brl / 5.12
print(f"You can buy ${round(dollar, 2)} dollars with R${round(brl, 2)}")
