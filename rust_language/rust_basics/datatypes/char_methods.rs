fn main() {
    let c: char = 'a';

    /*returns true if the character is alphabetic*/
    if c.is_alphabetic() {
        println!("{} is an alphabetic character.", c);
    }

    if c.is_numeric() {
        println!("{} is a numeric character.", c);
    } else {
        println!("{} is not a numeric character.", c);
    }

    for upper in c.to_uppercase() {
        println!("Uppercase of {} is {}", c, upper);
    }

    for lower in 'A'.to_lowercase() {
        println!("Lowercase of {} is {}", 'A', lower);
    }
}
