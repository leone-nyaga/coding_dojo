fn main() {
    print!("Hello, ");//no newline
    print!("World!");//continues on same line
    println!("");//adds newline

    let name = "Alice";
    let age = 30;
    print!("My name is {} and i am {} years old.", name, age);
    println!(); //adds newline

    let number = 42;
    print!("The number is: {}", number);
    println!();//adds newline
}
