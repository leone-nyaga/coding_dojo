fn main() {
    let a: f32 = 3.5;
    let b: f32 = 2.0;

    // Basic arithmetic operations
    println!("a + b = {}", a + b);
    println!("a - b = {}", a - b);
    println!("a * b = {}", a * b);
    println!("a / b = {}", a / b);

    // Using standard library functions
    println!("Square root of a: {}", a.sqrt());
    println!("Exponential of b: {}", b.exp());
    println!("Natural log of a: {}", a.ln());

    // Trigonometric functions
    let angle: f64 = std::f64::consts::PI / 4.0; // 45 degrees
    println!("Sine of 45 degrees: {}", angle.sin());
    println!("Cosine of 45 degrees: {}", angle.cos());

    // Handling precision in comparisons
    let x: f64 = 0.1 + 0.2;
    let y: f64 = 0.3;
    let tolerance: f64 = 1e-10;
    println!("x and y are approximately equal: {}", (x - y).abs() < tolerance);
}
