export default class Library {
  constructor(name, location) {
    this._name = name;
    this._location = location;
    this._books = [];
  }

  addBook(book) {
    this._books.push(book);
  }

  removeBook(bookTitle) {
    this._books = this._books.filter(book => book.getTitle() !== book.getTitle);
  }

  findBook(bookTitle) {
    this._books = this._books.find(book => book.getTitle() === bookTitle) || 'Book not found';
  }

  listBooks() {
    if (this.book._length === 0) {
      console.log("Book is not present in the library");
    } else {
      this._books.forEach(book => {
        console.log(book.getDetails());
      });
    }
  }
}
