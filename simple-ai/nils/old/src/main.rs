use projektarbeit_simple_ai::run;

fn main() {
    let result = run();
    if let Err(e) = result {eprint!("{}", e)};
}
