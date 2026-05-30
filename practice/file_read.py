def solution1(file_path: str = "D:\\Training\\data-science-roadmap\\data-structures-algorithms-python\\practice\\data\\nyc_weather.csv"):
    cur_row = 0
    data = {}
    keys = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if cur_row == 0:
                keys = line.split(',')
                for key in keys:
                    data.update({key: []})
            else:
                values = line.split(',')
                for i, value in enumerate(values):
                    data[keys[i]].append(value)
    date_to_temp = {}
    for i in range(len(data[keys[0]])):
        date_to_temp.update({data[keys[0]][i]: data[keys[1]][i]})
    print(f"Tempeature: {date_to_temp.get('Jan 1', 'Not found')}")
    print(f"max temp: max temp: {max(list(date_to_temp.values()))}")

def main():
    solution1()

if __name__ == "__main__":
    main()
