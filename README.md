# Book Library CLI

## Group Project

Welcome to the Book Library CLI project! This command-line interface (CLI) allows users to manage a book library efficiently. The application provides various features such as adding books, categorizing them by genre, tracking reading sessions, and offering book recommendations based on genres.

## Features

- Add a Book: Users can easily add new books to the library.
- Categorize by Genre: Organize books based on their genres for better management.
- Track Reading Sessions: Keep a record of reading sessions for each book.
- Genre-Based Recommendations: Receive personalized book recommendations according to the chosen genre.
- Add Readers: Maintain a list of readers who can interact with the library.



## Project Proposal link
https://docs.google.com/document/d/1bzhlarU3lFLDtevJZPt_-_D6prI-eVst-goBeD6fYd8/edit?usp=sharing



## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:StormRobert/Book-Library-CLI.git
   ```

2. Change into the project directory:

   ```bash
   cd book-library-cli
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application, you need Python 3 installed in your system.
Change into the app directory:

   ```bash
   cd app
   ```
Run the CLI application using the following command:

```bash
python3 bookLibrary.py show-library
```

### Commands

- `show-library`: Display the entire library, including books, users, and checkouts.
- `new_book`: Add a new book to the library.
- `modify_book`: Update information for an existing book.
- `remove_book`: Remove a book from the library.
- `new_user`: Add a new user to the library.
- `remove_user`: Remove a user from the library.
- `borrow_book`: Check out a book to a user.
- `finish_book`: Return a checked-out book.
- `similar_books`: Get book recommendations based on user history.

### Examples

- To view the entire library:

  ```bash
  python3 bookLibrary.py show-library
  ```

- To add a new book:

  ```bash
  python3 bookLibrary.py new_book "The Great Gatsby"  "F. Scott Fitzgerald" "1925-04-10" "Classic"
  ```

- To check out a book to a user:

  ```bash
  python3 bookLibrary.py borrow_book --book_id 1 --user_id 3 --genre "Mystery"
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to customize the information such as the repository URL, your username, and any other specific details related to your project. Add more sections or details as needed to provide comprehensive documentation for your CLI application.

# Contributors
Matthew Nderitu
Elijah Nyasiando
Faith Wahome

Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests.