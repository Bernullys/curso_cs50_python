import csv

def read_csv(path):
    with open(path, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        header = next(reader)
        #print(header)
        data = []
        for row in reader:
            iterable = zip(header, row)
            #print("++++++++" * 10)
            #print(list(iterable))
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

if __name__=="__main__":
    data = read_csv("./data.csv")
    print(data[10])