/*
 * finds the result of area of a square
 */
fn area_of_square(side:f64) {
    let area = side * side;

    println!("The side length is {}, and the Area is {}", side, area);
}

fn main() {
    let side = 15.6;
    area_of_square(side);
}
