def rectangle_area(length, width):
    """
    This function calculates the area of a rectangle.
    It takes two parameters: length and width.
    It returns: area = length x width
    """
    return length * width


l = float(input("Enter length: "))
w = float(input("Enter width: "))
area = rectangle_area(l, w)
print("\nArea of rectangle:", area)
