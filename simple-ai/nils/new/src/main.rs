use std::io;
use colore_ai_neuroflow::{self, commandinput, Commands, load_data};
use neuroflow::{FeedForward, data, activators};
use neuroflow::data::DataSet;
use neuroflow::activators::Type::Tanh;

fn main() {
    let e = run();
    match e {
        Ok(_) => println!("Alles ist in ordnung"),
        Err(e) => eprint!("{}", e),
    }
}

pub fn run() -> io::Result<()> {
    let mut exit = false;
    let mut nn: FeedForward = FeedForward::new(&[1,1]);
    nn.activation(Tanh);
    let mut data = DataSet::new();
    while exit == false {
        match commandinput() {
            Ok(Commands::Load(p)) => {
                nn = neuroflow::io::load(&p).unwrap();
            },
            Ok(Commands::Thinkm(i)) => {
                let results: &[f64] = nn.calc(&i);
                for result in results {
                    println!("{}", result);
                }
            },
            Ok(Commands::Exit) => exit = true,
            Ok(Commands::Save(p)) => { match neuroflow::io::save(&mut nn, &p) {
                Ok(_) => println!("saved"),
                Err(_) => eprintln!("Saving faild"),
            }},
            Ok(Commands::New(i)) => {
                nn = FeedForward::new(&i);
            },
            Ok(Commands::LoadData(p)) => data = load_data(p)?,
            Ok(Commands::Learn((lr, i))) => {
                nn.learning_rate(lr)
                    .train(&data, i)
            }
            Err(e) if e.kind() == io::ErrorKind::InvalidInput => eprintln!("{}", e),
            Err(e) => return Err(e)
        }
    }
    return Ok(());
}