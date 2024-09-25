import Book from './book-class';
import Library from './library-class';

const book1 = new Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 5);
const book2 = new Book("To Kill a Mockingbird", "Harper Lee", 1960, 3);
const book3 = new Book("1984", "George Orwell", 1949, 7);

const cityLibrary = new Library("City Library", "Downtown");

cityLibrary.addBook(book1);
cityLibrary.addBook(book2);
cityLibrary.addBook(book3);

console.log("Books available in the library:");
cityLibrary.listBooks();
