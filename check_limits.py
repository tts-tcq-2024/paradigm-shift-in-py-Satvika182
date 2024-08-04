
def translate_to_common_units():
    return {
        "temperature": {
            "LOW_BREACH": 0,
            "LOW_WARNING": 0 + 0.05 * 45,
            "NORMAL_LOW": 0 + 0.05 * 45,
            "NORMAL_HIGH": 45 - 0.05 * 45,
            "HIGH_WARNING": 45 - 0.05 * 45,
            "HIGH_BREACH": 45,
        },
        "soc": {
            "LOW_BREACH": 20,
            "LOW_WARNING": 20 + 0.05 * 80,
            "NORMAL_LOW": 20 + 0.05 * 80,
            "NORMAL_HIGH": 80 - 0.05 * 80,
            "HIGH_WARNING": 80 - 0.05 * 80,
            "HIGH_BREACH": 80,
        },
        "charge_rate": {
            "LOW_BREACH": 0,
            "NORMAL_HIGH": 0.8 - 0.05 * 0.8,
            "HIGH_WARNING": 0.8 - 0.05 * 0.8,
            "HIGH_BREACH": 0.8,
        }
    }

def map_to_ranges(value, boundaries):
    if value < boundaries["LOW_BREACH"]:
        return "BREACH_LOW"
    elif value < boundaries["LOW_WARNING"]:
        return "WARNING_LOW"
    elif value <= boundaries["NORMAL_HIGH"]:
        return "NORMAL"
    elif value <= boundaries["HIGH_WARNING"]:
        return "WARNING_HIGH"
    elif value <= boundaries["HIGH_BREACH"]:
        return "BREACH_HIGH"
    else:
        return "BREACH_HIGH"

def translate_anomaly_to_message(parameter, condition):
    messages = {
        "temperature": {
            "BREACH_LOW": "Temperature is out of range!",
            "BREACH_HIGH": "Temperature is out of range!",
            "WARNING_LOW": "Warning: Approaching low temperature limit",
            "WARNING_HIGH": "Warning: Approaching high temperature limit",
            "NORMAL": ""
        },
        "soc": {
            "BREACH_LOW": "State of Charge is out of range!",
            "BREACH_HIGH": "State of Charge is out of range!",
            "WARNING_LOW": "Warning: Approaching discharge",
            "WARNING_HIGH": "Warning: Approaching charge-peak",
            "NORMAL": ""
        },
        "charge_rate": {
            "BREACH_HIGH": "Charge rate is out of range!",
            "WARNING_HIGH": "Warning: Approaching charge rate peak",
            "NORMAL": ""
        }
    }
    return messages[parameter][condition]

def compute_battery_status(temperature, soc, charge_rate):
    boundaries = translate_to_common_units()

    temp_condition = map_to_ranges(temperature, boundaries["temperature"])
    soc_condition = map_to_ranges(soc, boundaries["soc"])
    charge_rate_condition = map_to_ranges(charge_rate, boundaries["charge_rate"])

    temp_message = translate_anomaly_to_message("temperature", temp_condition)
    soc_message = translate_anomaly_to_message("soc", soc_condition)
    charge_rate_message = translate_anomaly_to_message("charge_rate", charge_rate_condition)

    messages = [temp_message, soc_message, charge_rate_message]
    for message in messages:
        if message:
            print(message)

    if temp_condition.startswith("BREACH") or soc_condition.startswith("BREACH") or charge_rate_condition.startswith("BREACH"):
        return False

    return True

def battery_is_ok(temperature, soc, charge_rate):
    return compute_battery_status(temperature, soc, charge_rate)


if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
    assert(battery_is_ok(3, 21, 0.75) is True)  # Expect warning for temperature and SoC
    assert(battery_is_ok(43, 79, 0.8) is True)  # Expect warning for temperature, SoC, and charge rate
    assert(battery_is_ok(22, 76, 0.78) is True)  # Expect warning for SoC and charge rate
