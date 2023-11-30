def is_numeric(value):
    """Checks if the provided value is numeric."""
    try:
        float(value)
        return True
    except ValueError:
        return False