def is_within_range(value, min_val, max_val):
    """
    Check if the value is within the given range [min_val, max_val].
    Returns True if the value is within range, otherwise False.
    """
    return (min_val is None or value >= min_val) and (max_val is None or value <= max_val)

def is_approaching_limit(value, min_val, max_val, tolerance):
    """
    Check if the value is approaching the min_val or max_val, within the given tolerance.
    Returns True if the value is within the tolerance range, otherwise False.
    """
    return ((min_val is not None and min_val <= value <= min_val + tolerance) or
            (max_val is not None and max_val - tolerance <= value <= max_val))

def calculate_tolerance(reference_value, tolerance_percentage=5):
    """
    Calculate tolerance as a percentage of a reference value.
    Default tolerance percentage is 5%.
    Returns the tolerance value.
    """
    return reference_value * tolerance_percentage / 100
