# Currency Converter

This project is a Currency Converter application built using the `customtkinter` library for the GUI and `requests` for fetching real-time exchange rates. The application allows users to convert amounts between different currencies based on the latest exchange rates.

## Features

- Convert amounts between various currencies.
- Fetches real-time exchange rates from an external API.
- Easy-to-use graphical interface.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/LiveKiller/currency-convert.git
   cd currency-converter
   ```

2. **Install dependencies:**

   This project requires Python and the following Python libraries:
   
   - customtkinter
   - requests

   You can install them using pip:

   ```bash
   pip install customtkinter requests
   ```

3. **Ensure you have an active internet connection** to fetch the latest exchange rates from the API.

## Usage

1. **Run the application:**

   ```bash
   python main.py
   ```

2. **Interacting with the Currency Converter:**

   - **Amount:** Enter the amount you wish to convert.
   - **From:** Select the currency you are converting from.
   - **To:** Select the currency you are converting to.
   - **Convert:** Click the "Convert" button to perform the conversion. The result will be displayed below.

## File Structure

- `main.py`: The main application file containing the GUI and conversion logic.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements

- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [requests](https://requests.readthedocs.io/en/master/)

Feel free to customize this `README.md` file to better fit your specific needs and project details.