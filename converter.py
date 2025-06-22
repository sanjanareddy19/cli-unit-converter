import argparse
from typing import Union

class TemperatureConverter:
    """A class to handle temperature conversions between Celsius and Fahrenheit."""
    
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def convert(value: float, unit: str) -> tuple[float, str]:
        """
        Convert temperature between Celsius and Fahrenheit.
        
        Args:
            value: Temperature value to convert
            unit: Original unit ('c' or 'f')
            
        Returns:
            tuple: (converted_value, target_unit)
        """
        if unit.lower() == 'c':
            return TemperatureConverter.celsius_to_fahrenheit(value), 'F'
        elif unit.lower() == 'f':
            return TemperatureConverter.fahrenheit_to_celsius(value), 'C'
        else:
            raise ValueError("Invalid unit. Use 'C' or 'F'")

def parse_arguments():
    """Setup and parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Temperature Conversion Tool',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""Examples:
  python converter.py -c 25
  python converter.py --celsius 25
  python converter.py -f 77
  python converter.py --fahrenheit 77"""
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-c', '--celsius',
        type=float,
        help='Temperature in Celsius to convert to Fahrenheit'
    )
    group.add_argument(
        '-f', '--fahrenheit',
        type=float,
        help='Temperature in Fahrenheit to convert to Celsius'
    )
    
    parser.add_argument(
        '-p', '--precision',
        type=int,
        default=2,
        choices=range(0, 6),
        help='Decimal places for output (0-5, default: 2)'
    )
    
    return parser.parse_args()

def main():
    """Main function to execute the temperature conversion."""
    try:
        args = parse_arguments()
        
        if args.celsius is not None:
            value, unit = TemperatureConverter.convert(args.celsius, 'c')
            original_unit = 'C'
            original_value = args.celsius
        else:
            value, unit = TemperatureConverter.convert(args.fahrenheit, 'f')
            original_unit = 'F'
            original_value = args.fahrenheit
        
        print(f"{original_value}°{original_unit} = {value:.{args.precision}f}°{unit}")
    
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()