/*
 * using step by method to skip over a certain number
 */
fn main() {
    for number in (1..=15).step_by(2) {
        println!("The number is {}!", number);
    }
}
