
def battery_is_ok(temperature, soc, charge_rate):
    conditions = [
        (0 <= temperature <= 45, 'Temperature is out of range!'),
        (20 <= soc <= 80, 'State of Charge is out of range!'),
        (charge_rate <= 0.8, 'Charge rate is out of range!')
    ]

    for condition, message in conditions:
        if not condition:
            print(message)
            return False

  return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
