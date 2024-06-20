/*
 * multiplication table for 9
 */
fn main() {
    let num = 9;

    for i in 1..=10 {
        println!("{} x {} = {}", i, num, i * num);
    }
}
