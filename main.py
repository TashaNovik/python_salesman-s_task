# 4 города:
# Варианты путешествия с возвращением домой:

if __name__ == '__main__':

    one_two = 10
    two_one = 10
    one_three = 15
    three_one = 15
    two_three = 35
    three_two = 35
    two_four = 25
    four_two = 25
    four_one = 20
    one_four = 20
    four_three = 30
    three_four = 30

    list_ways = {}
    way_1  = "3 1 4 2 3"
    cost_1 = three_one + one_four + four_two + two_three
    list_ways[way_1] = cost_1
    way_2 = "3 1 2 4 3"
    cost_2 = three_one + one_two + two_four + four_three
    list_ways[way_2] = cost_2
    way_3 = "3 2 1 4 3"
    cost_3 = three_two + two_one + one_four + four_three
    list_ways[way_3] = cost_3
    way_4 = "3 2 4 1 3"
    cost_4 = three_two + two_four + four_one + one_three
    list_ways[way_4] = cost_4
    way_5 = "3 4 1 2 3"
    cost_5 = three_four + four_one + one_two + two_three
    list_ways[way_5] = cost_5
    way_6 = "3 4 2 1 3"
    cost_6 = three_four + four_two + two_one + one_three
    list_ways[way_6] = cost_6

    min_cost = min(list_ways.values())

    for key, value in list_ways.items():
        if value == min_cost:
            print("Маршруты с минимальной стоимостью: ")
            print(key + " =", value)
