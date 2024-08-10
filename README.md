# Daily Quote FastAPI

Welcome to **Daily Quote FastAPI**! 
This project is a web application that fetches and displays a new inspirational quote each day. 
It uses FastAPI for the backend, `requests` and `BeautifulSoup` for web scraping, and HTML/CSS for the frontend. 
The FastAPI app handles the scraping and serves the quote to users.

## Features

- **Daily Quote Retrieval**: Automatically fetches a new inspirational quote each day.
- **FastAPI Backend**: Efficiently handles API requests and serves dynamic content.
- **HTML/CSS Frontend**: Provides a clean and user-friendly interface to display the quote, author, and date.

## Getting Started

To set up and run this project locally, follow these steps:

1. **Clone the Repository**: Clone the repository using `git clone https://github.com/christian759/daily_quote_fastapi.git` and navigate into the directory with `cd daily_quote_fastapi`.

2. **Create and Activate a Virtual Environment**: Create and activate a virtual environment with `python -m venv venv` and `source venv/bin/activate` (or `venv\Scripts\activate` on Windows).

3. **Install Required Packages**: Install the necessary packages by running `pip install -r requirements.txt`.

4. **Run the FastAPI Server**: Start the FastAPI server with `uvicorn main:app --reload`.

5. **Access the Application**: Open your web browser and go to `http://localhost:8000` to view the daily quote.

## Application Summary

The FastAPI application consists of a single script, `main.py`, which handles both the web scraping and serving of quotes. It uses `requests` and `BeautifulSoup` to scrape quotes from an external website. The `write_notification` function fetches the quote, author, and date, which are then displayed on the homepage. The `/` endpoint processes requests, performs background scraping, and renders the quote using an HTML template.

## Technologies Used

- **Backend**: FastAPI
- **Web Scraping**: `requests`, `BeautifulSoup`
- **Frontend**: HTML, CSS
- **Server**: Uvicorn

## Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository.
2. **Create** a new branch with `git checkout -b feature/your-feature`.
3. **Commit** your changes with `git commit -am 'Add new feature'`.
4. **Push** to your branch with `git push origin feature/your-feature`.
5. **Open** a Pull Request to merge your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, you can contact:

- **Name**: Eighemhenrio Chrisitian
- **Email**: christian4onos@gmail.com
- **GitHub**: [christian759](https://github.com/christian759)
- **Whatsapp**: +2347016029291

Feel free to explore, contribute, and enjoy the application!
