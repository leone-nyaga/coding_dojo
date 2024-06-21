/*
 * function to print area of rectangle
 */
fn area_of_rectangle(length:f64, width:f64) {
    let area = length * width;

    println!("The length is {}, The width is {}, The area is {:.3}!", length, width, area);
}

fn main() {
    let length = 19.8;
    let width = 14.2;

    area_of_rectangle(length, width);
}
