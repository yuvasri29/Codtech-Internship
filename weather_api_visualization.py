import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "YOUR_API_KEY"

cities = ["Chennai", "Delhi", "Mumbai", "Bangalore", "Hyderabad"]

temperature = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if "main" in data:
        temperature.append(data["main"]["temp"])
    else:
        temperature.append(None)

df = pd.DataFrame({
    "City": cities,
    "Temperature": temperature
})

print(df)
sns.barplot(x="City", y="Temperature", data=df)
plt.title("Temperature of Cities")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.show()