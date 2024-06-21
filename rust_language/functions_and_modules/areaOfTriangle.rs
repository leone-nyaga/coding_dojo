/* 
 * prints the area of a triangle
 */
fn areaOfTriangle(base:f64, height:f64) {
    let area = 0.5 * base * height;

    println!("The Base is {}, The Height is {}, Area of the Triangle is {}", base, height, area);
}

fn main() {
    let base = 21.0;
    let height = 15.2;

    areaOfTriangle(base, height);
}
