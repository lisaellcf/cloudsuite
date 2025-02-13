# CloudSuite

CloudSuite is a Python-based program designed to monitor and control network usage on Windows systems to prevent excessive bandwidth consumption. It alerts users when their network usage exceeds a specified threshold, helping to manage and optimize bandwidth usage effectively.

## Features

- Monitors network usage in real-time.
- Alerts users when bandwidth consumption exceeds a predefined limit.
- Provides an easy-to-use interface with warning messages for better network management.

## Requirements

- Python 3.x
- `psutil` library for accessing system and network information.

## Installation

1. Clone the repository or download the `cloudsuite.py` file.
2. Install the required Python library by running:
   ```bash
   pip install psutil
   ```

## Usage

1. Open a terminal or command prompt.
2. Run the program with Python:
   ```bash
   python cloudsuite.py
   ```
3. Set your desired bandwidth limit in the code (default is 500 MB).
4. The program will monitor network usage and alert you when the limit is exceeded.

## Configuration

- To change the bandwidth limit, modify the `bandwidth_limit_mb` variable in the `__main__` section of the `cloudsuite.py` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or bug fixes.

## Disclaimer

CloudSuite is intended for personal use and educational purposes. It may not be suitable for all environments or requirements. Use it at your own risk.