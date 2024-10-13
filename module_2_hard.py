def generate_password(n):
    
    if n < 3 or n > 20:
        return "Число должно быть в диапазоне от 3 до 20."


    result_pairs = []


    for i in range(1, 21):
        for j in range(i, 21):
            pair_sum = i + j
            if n % pair_sum == 0:
                pair_str = f"{i}{j}"
                result_pairs.append(pair_str)


    result = ''.join(result_pairs)
    return result



for n in range(3, 21):
    password = generate_password(n)
    print(f"{n} - {password}")
