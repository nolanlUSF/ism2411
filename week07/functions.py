# -- Exercise 1 --
#Define calculate tax function

def calculate_tax(price,rate):
    return price* rate

# calling the function

tax1 = calculate_tax(100, 0.07 )
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

# -- Exercise 2 --

def apply_discount(price, tier):
    if tier == "Gold":
        return price * 0.85
    elif tier == "Silver":
        return price * 0.90
    elif tier == "Bronze":
        return price * 0.95
    else:
        return price

price = 200
tiers = ["Gold", "Silver", "Bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

discounted = apply_discount(200, "Gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'Gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "Gold"), (150, "Silver"), (100, "Bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# exercise 5
for price in price:
    if price > 400:
        print(f"Alert: Outlier found - ${price}. Stopping.")
        break
    if price <= 100:
        continue
    print(f"${sale}")

# exercise 6

x = 100 # Global

def double_it():
    x = 999 # Local
    return x * 2

print(x)
print(double_it())
print(x)

