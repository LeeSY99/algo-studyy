fn main() {
    let mut a = 1;
    let mut b = 5;
    let mut c = 3;

    a += b;
    b -= c;

    println!("{}", a);
    println!("{}", b);
    println!("{}", c);
}