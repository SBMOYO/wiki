# Django Wiki Clone

This project is a simple wiki clone built using the Django framework and SQLite database.

## Features

- Create and edit wiki entries using Markdown.
- Entries are automatically converted from Markdown to HTML for display.

## Installation

1. Clone the repository: git clone https://github.com/SBMOYO/wiki.git

2. Navigate to the project directory: cd wiki

3. Install the required packages: pip install -r requirements.txt

4. Run the migrations: python manage.py migrate

5. Start the server: python manage.py runserver


Now, you can navigate to `localhost:8000` in your browser to see the application in action.

## Usage

To create a new wiki entry, navigate to the `/new%20page` route and enter your content in Markdown format. When you save the entry, it will be stored in the database and displayed in HTML format.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under a free License.




