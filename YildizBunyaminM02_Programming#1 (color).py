
"""Created on Sat Mar 30 15:23:52 2024

Author: Bunyamin Fuat Yildiz 

    Mixes two primary colors and returns the resulting secondary color.

Args:
    color1 :  first primary color.
    color2 : second primary color.
"""


def mix_colors(color1, color2):
    
    
    colors = ["red", "blue", "yellow"]
    if color1.lower() not in colors or color2.lower() not in colors:
        return "Error: Please enter valid primary colors (red, blue, yellow)."

    result = ""
    if (color1.lower() == "red" and color2.lower() == "blue") or (color1.lower() == "blue" and color2.lower() == "red"):
        result = "purple"
    elif (color1.lower() == "red" and color2.lower() == "yellow") or (color1.lower() == "yellow" and color2.lower() == "red"):
        result = "orange"
    else:
        result = "green"

    return result 


def main():
    # Get user input
    color1 = input("Enter the first primary color: ")
    color2 = input("Enter the second primary color: ")

    # Display the result
    print("Mixing", color1, "and", color2, "results in", mix_colors(color1, color2))


if __name__ == "__main__":
    main()
