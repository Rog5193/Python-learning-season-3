def price_and_quality(n):
    pairs_dict = {}
    for i in range(n):
        # Assuming input is something like: product_name price quality
        key, price, quality = input(f"Enter pair {i+1} (product name price quality): ").split()
        pairs_dict[key] = (int(price), int(quality))  # Store price and quality as a tuple
    return pairs_dict

def compare_price(pairs_dict):
    # Extract prices and qualities from the dictionary
    prices = [x[0] for x in pairs_dict.values()]  # Extract all the prices
    qualities = [x[1] for x in pairs_dict.values()]  # Extract all the qualities

    # Compare each pair of prices and qualities
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] >= prices[j] and qualities[i] >= qualities[j]:
                print(f"Yes! Price {prices[i]} and Quality {qualities[i]} >= Price {prices[j]} and Quality {qualities[j]}")
            else:
                print(f"No! Price {prices[i]} and Quality {qualities[i]} < Price {prices[j]} and Quality {qualities[j]}")

# Example usage
n = int(input("How many pairs do you want to enter? "))
pairs = price_and_quality(n)
compare_price(pairs)