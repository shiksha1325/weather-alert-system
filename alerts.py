def get_alert(temp, rainfall, humidity):
    alerts = []

    if temp > 40:
        alerts.append("⚠️ Heatwave Alert")
    if temp < 5:
        alerts.append("⚠️ Cold Wave Alert")
    if rainfall > 100:
        alerts.append("⚠️ Flood Risk Alert")
    if humidity > 85 and temp > 30:
        alerts.append("⚠️ High Humidity Alert")

    if not alerts:
        alerts.append("✅ Normal Weather")

    return alerts