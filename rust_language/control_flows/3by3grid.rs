/*
 * prints a 3 x 3 grid
 */
fn main() {
    for i in 0..=3 {
        for j in 0..=3 {
            println!("({}, {})", i, j);
        }
        println!();
    }
}
