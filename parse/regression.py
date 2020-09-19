import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


def read_file_csv(path):
    return pd.read_csv(path, encoding='utf-16')


def delete_unnecessary_data(price_room):
    price_room.index = pd.to_datetime(price_room['update'])
    price_room = price_room.drop(['update', 'link', 'prise_BYN'], axis=1)
    return price_room


def validation_data(price_room):
    for i in price_room.isna().any():
        if i == False:
            price_room = price_room.dropna()
    return price_room

def creating_scatterplot(price_room):
    x = sorted(price_room['prise_USD'])
    y = sorted(price_room['room'])
    plt.plot(x, y, 'o', color='cadetblue', label='Daily Price')
    plt.title("Apartments for rent")
    plt.xlabel("Prise_USD")
    plt.ylabel("Room")
    plt.legend()
    plt.show()


def main():
    path = r'..\resources\data_csv2020-09-16.csv'
    price_room = read_file_csv(path)

    price_room = validation_data(delete_unnecessary_data(price_room))
    creating_scatterplot(price_room)
main()