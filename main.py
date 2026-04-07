import matplotlib.pyplot as plt
from alerts import get_alert
from data_handler import create_dataframe, add_data

def main():
    data = create_dataframe()

    print("===================================")
    print("   WEATHER ALERT SYSTEM 🌦️")
    print("===================================")

    while True:
        city = input("\nEnter city: ")

        try:
            temp = float(input("Temperature (°C): "))
            rainfall = float(input("Rainfall (mm): "))
            humidity = float(input("Humidity (%): "))
        except ValueError:
            print("❌ Invalid input!")
            continue

        data = add_data(data, city, temp, rainfall, humidity)

        alerts = get_alert(temp, rainfall, humidity)

        print("\nAlerts:")
        for alert in alerts:
            print(alert)

        choice = input("\nAdd more data? (yes/no): ").lower()
        if choice != "yes":
            break

    print("\nCollected Data:\n", data)

    # Graphs
    plt.figure()
    plt.plot(data["Temperature"], marker='o')
    plt.title("Temperature Trend")
    plt.xlabel("Entry Index")
    plt.ylabel("Temperature")
    plt.show()

    plt.figure()
    plt.plot(data["Rainfall"], marker='o')
    plt.title("Rainfall Trend")
    plt.xlabel("Entry Index")
    plt.ylabel("Rainfall")
    plt.show()

    plt.figure()
    plt.plot(data["Humidity"], marker='o')
    plt.title("Humidity Trend")
    plt.xlabel("Entry Index")
    plt.ylabel("Humidity")
    plt.show()


if __name__ == "__main__":
    main()