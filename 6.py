def A_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "YOU DIED"
    return round(sum(list_num) / len(list_num), 2)
test_cases = [
    ([1, 1], 1),
    ([2.5, 3.5], 3),
    ([1, 2, 3], 2.0),
    ([10, 20, 30], 20.0),
    ([1, '2'], 1.5),
    ([1.5, '2'], 1.75),
    ([1, 'abc'], "YOU DIED"),
    ([3, 4], 3.5),
    ([0, 0, 0], 0.0),
    ([None, 1], "YOU DIED")
]
for inp, expected in test_cases:
    result = A_num(inp)
    print(f"A_num({inp}) = {result} | ожидаемо: {expected}")
    assert result == expected
print("Все тесты прошли успешно!")
