/*
 * converting integer to float
 */
fn main() {
    let number: u16 = 90;

    let float_number = number as f64;
    
    println!("Original value: {}", number);
    println!("New value: {}", float_number);
}
