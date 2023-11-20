def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Ejemplo de uso 1:
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
resultado1 = max_area(height1)
print(resultado1)  

# Ejemplo de uso 2:
height2 = [1, 1]
resultado2 = max_area(height2)
print(resultado2)  