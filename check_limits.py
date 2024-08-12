from utils import is_within_range, is_approaching_limit, calculate_tolerance

class BatteryMonitor:
    def __init__(self):
        # Define parameter configurations using a dictionary
        self.parameters = {
            'temperature': {'min_val': 0, 'max_val': 45, 'tolerance': calculate_tolerance(45)},
            'soc': {'min_val': 20, 'max_val': 80, 'tolerance': calculate_tolerance(80)},
            'charge_rate': {'min_val': None, 'max_val': 0.8, 'tolerance': calculate_tolerance(0.8)},
        }
        
        # Initialize with all warnings enabled
        self.warning_config = {key: True for key in self.parameters}
        self.warning_messages = {
            'temperature': 'Temperature is out of range!',
            'soc': 'State of Charge (SOC) is out of range!',
            'charge_rate': 'Charge rate is out of range!'
        }

    def should_warn(self, limit_type, value):
        param_config = self.parameters[limit_type]
        return (self.warning_config.get(limit_type, False) and
                is_approaching_limit(value, param_config['min_val'], param_config['max_val'], param_config['tolerance']))

    def check_limits(self, limit_type, value):
        param_config = self.parameters[limit_type]
        warning_needed = self.should_warn(limit_type, value)
        value_ok = is_within_range(value, param_config['min_val'], param_config['max_val'])
        return value_ok, warning_needed

    def handle_warnings(self, is_parameter_within_limits, is_approaching_limit_alert, parameter_name):
        if is_approaching_limit_alert:
            print(f'Warning: Approaching {parameter_name} limit')
        elif not is_parameter_within_limits:
            print(self.warning_messages.get(parameter_name.lower(), 'Unknown parameter is out of range!'))

    def battery_is_ok(self, temperature, soc, charge_rate):
        temp_ok, temp_warning = self.check_limits('temperature', temperature)
        soc_ok, soc_warning = self.check_limits('soc', soc)
        charge_rate_ok, charge_rate_warning = self.check_limits('charge_rate', charge_rate)

        self.handle_warnings(temp_ok, temp_warning, 'Temperature')
        self.handle_warnings(soc_ok, soc_warning, 'State of Charge (SOC)')
        self.handle_warnings(charge_rate_ok, charge_rate_warning, 'Charge rate')

        return temp_ok and soc_ok and charge_rate_ok

    def configure_warnings(self, temperature=True, soc=True, charge_rate=True):
        self.warning_config['temperature'] = temperature
        self.warning_config['soc'] = soc
        self.warning_config['charge_rate'] = charge_rate

    def show_configurations(self):
        print('Current warning configurations:')
        for param, enabled in self.warning_config.items():
            status = 'Enabled' if enabled else 'Disabled'
            print(f'{param.capitalize()}: {status}')

if __name__ == '__main__':
    monitor = BatteryMonitor()
    monitor.configure_warnings(temperature=False)  # Example configuration
    monitor.show_configurations()
