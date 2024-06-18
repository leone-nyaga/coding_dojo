/*
 * Basic nested if statement
 */

fn main() {
    let number = -2;

    if number > 0 {
        println!("The number is positive");
    } else {
        if number < 0 {
            println!("The number is negative.");
        } else {
            println!("The number is zero!");
        }
    }
}
