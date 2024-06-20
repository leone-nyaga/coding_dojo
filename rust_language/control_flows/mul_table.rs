/*
 * prints multiplication table
 */
fn main() {
    for i in 1..=10 {
        for j in 1..=10 {
            println!("{:4}", i*j);
        }
        println!();
    }
}
