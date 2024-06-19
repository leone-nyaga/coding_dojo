/*
 * prints the first 4 lines
 * of the song bootylicious by Destiny's Child
 */

fn main() {
    let names = ["Kelly", "Michelle", "Beyonce"];

    let phrase = "can you handle this?";

    for singer in &names {
        println!("{} , {}", singer, phrase);
    }
    println!("I don't think they can handle this!");
}
