use std::io;

fn sieve(x: usize) -> Vec<bool> {
    let mut vec = Vec::new();
    for val in 0..x + 1 {
        vec.push(match val {
            0 => false,
            1 => false,
            _ => true,
        });
    }
    for i in 2..x + 1 {
        if vec[i] {
            for j in (i * i..x + 1).step_by(i) {
                vec[j] = false;
            }
        }
    }
    vec
}

fn main() {
    println!("Enter a maximum value:");
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Unable to read value");
    input.pop();
    let max_val = input.parse::<usize>().unwrap();
    let is_prime = sieve(max_val);
    println!("All primes up to {}", max_val);
    for i in 0..is_prime.len() {
        if is_prime[i] {
            println!("{} ", i);
        }
    }
}
