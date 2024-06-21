/*
 * function to add two numbers
 */
fn main() {
    let result = add(5, 3);
    println!("The sum is {}", result);
}

fn add(x:i32, y:i32) -> i32 {
    x + y
}
