// use std::io;
use colore_ai_neuroflow::{self, commandinput, Commands, load_data};
use neuroflow::{FeedForward, data, activators};
use neuroflow::data::DataSet;
use neuroflow::activators::Type::Tanh;

// use std::net::{TcpListener, SocketAddr};
// use http::{Request, Response, StatusCode};

use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

use httparse;


fn main() {

    let mut nn: FeedForward = FeedForward::new(&[1,1]);
    nn.activation(Tanh);
    let mut data = DataSet::new();
    
    nn = neuroflow::io::load("20231211_cai").unwrap();

        // let i: Vec<f64> = vec![1.0, 1.0, 1.0];
        let mut i: Vec<f64> = Vec::new();

        let input = fs::read_to_string("input.txt").unwrap();

        for line in input.split(";") {
            i.push(line.parse::<f64>().unwrap());
        }

        let result: &f64 = nn.calc(&i).first().unwrap();

        println!("Result: {}", result);

        fs::write("result.txt", format!("{}", result)).unwrap();

}

// pub fn run() -> io::Result<()> {

//     // while exit == false {
//     //     match commandinput() {
//     //         Ok(Commands::Load(p)) => {
//     //             nn = neuroflow::io::load(&p).unwrap();
//     //         },
//     //         Ok(Commands::Thinkm(i)) => {
//     //             let results: &[f64] = nn.calc(&i);
//     //             for result in results {
//     //                 println!("{}", result);
//     //             }
//     //         },
//     //         Ok(Commands::Exit) => exit = true,
//     //         Ok(Commands::Save(p)) => { match neuroflow::io::save(&mut nn, &p) {
//     //             Ok(_) => println!("saved"),
//     //             Err(_) => eprintln!("Saving faild"),
//     //         }},
//     //         Ok(Commands::New(i)) => {
//     //             nn = FeedForward::new(&i);
//     //         },
//     //         Ok(Commands::LoadData(p)) => data = load_data(p)?,
//     //         Ok(Commands::Learn((lr, i))) => {
//     //             nn.learning_rate(lr)
//     //                 .train(&data, i)
//     //         }
//     //         Err(e) if e.kind() == io::ErrorKind::InvalidInput => eprintln!("{}", e),
//     //         Err(e) => return Err(e)
//     //     }
//     // }
//     return Ok(());
// }