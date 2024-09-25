export default class Book {
  constructor(title, author, yearPublished, copies) {
    this._title = title;
    this._author = author;
    this._yearPublished = yearPublished;
    this._copies = copies;
  }

  getTitle() {
    return this._title;
  }

  getDetails() {
    return `${this._title} by ${this._author} published in ${this._yearPublished}.`;
  }

  updatedCopies(newCopies) {
    this._copies = newCopies;
  }

  getCopies() {
    return this._copies;
  }
}
