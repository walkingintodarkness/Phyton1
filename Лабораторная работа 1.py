numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
i = numbers.index(None)
numbers[i] = (numbers[i-1] + numbers[i+1]) / 2
print("Измененный список:", numbers)
