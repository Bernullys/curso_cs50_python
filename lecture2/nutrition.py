select_fruit = input("Item: ").casefold()
fruits_calories = {
    "apple": 130,
    "avocado": 50,
    "Banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tengerine": 50,
    "watermelon": 80
}

for fruits in fruits_calories:
    if fruits == select_fruit:
        print("Calories: ", fruits_calories[fruits])