def min_candies(hunger):
    n = len(hunger)
    candies = [1] * n

    for i in range(1, n):
        if hunger[i] > hunger[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(n-2, -1, -1):
        if hunger[i] > hunger[i+1] and candies[i] <= candies[i+1]:
            candies[i] = candies[i+1] + 1
    
    return sum(candies)

# Ejemplo de uso:
hunger = [1, 0, 2]
resultado = min_candies(hunger)
print(resultado)  

hunger = [1, 2, 2]
resultado = min_candies(hunger)
print(resultado)  