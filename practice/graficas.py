# import matplotlib.pyplot as plt

# def generate_bar_chart():
#     labels = ["a", "b", "c"]
#     values = [100, 200, 80]


#     fig, ax = plt.subplots()
#     ax.bar(labels, values)
#     plt.show()

# generate_bar_chart()

original = [1, 2, 3, 4, 5]

#new = list(map(lambda x: x *2, original))
new = list(lambda x: x*2, original)

print(new)