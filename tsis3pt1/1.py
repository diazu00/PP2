def grams_to_ounces(grams):
    """
    Convert grams to ounces using the conversion factor 1 gram = 0.03527396 ounces.

    Args:
    - grams (float): The weight in grams.

    Returns:
    - float: The equivalent weight in ounces.
    """
    ounces = 0.03527396 * grams
    return ounces

grams_amount = float(input("grams:"))
ounces_result = grams_to_ounces(grams_amount)
print(f"{grams_amount} grams is equal to {ounces_result:.2f} ounces.")
