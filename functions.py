from datetime import datetime

from matplotlib import pyplot as plt


def prompt():
    """Prompt user for which file to open"""

    message = "We have 3 files containing weather data for 2014 "
    message += "Which file would you like to see\n A: Sitka, Alaska\n B: " \
               "Sitka, Alaska 2014\n C: Death Vally CA\n You can type 'q' to " \
               "exit program \n Enter: "

    filename = ''
    keep = True
    while keep:
        prompt = input(message)
        if prompt.title() == 'Q':
            keep = False
        elif prompt.title() == 'A':
            filename = "sitka_weather_07-2014.csv"
        elif prompt.title() == 'B':
            filename = "sitka_weather_2014.csv"
        elif prompt.title() == 'C':
            filename = "death_valley_2014.csv"
        else:
            print("Enter in only 'A', 'B', 'C' \n")
            continue
        print(filename)
        return filename


def graph_values(reader, dates, highs, lows):
    """Store the graph values of when the high, low temp occured"""
    for row in reader:
        current_date = ''
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')

        else:
            # Date
            dates.append((current_date))
            # Max Temp
            highs.append(high)
            # Min Temp
            lows.append(low)


def plot_graph(dates, highs, lows):
    """Visual rep of the graph info"""
    # PLot the data
    fig = plt.figure(dpi=128, figsize=(15, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()

    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()
