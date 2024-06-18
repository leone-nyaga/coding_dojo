/*
 * basic if statement with logical operators
 */
fn main() {
    let number = 6;

    if number % 2 == 0 && number % 3 == 0 {
        println!("The number is divisible by 2 and 3!");
    } else if number % 2 == 0 {
        println!("The number is divisible by 2!");
    } else if number % 3 == 0 {
        println!("The number is divisible by 3!");
    } else {
        println!("The number is not divisible by 2 or 3!");
    }
}
