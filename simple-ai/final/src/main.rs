use colore_ai_neuroflow::{self, commandinput, Commands, load_data};
use neuroflow::{FeedForward, data, activators};
use neuroflow::data::DataSet;
use neuroflow::activators::Type::Tanh;

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

        let mut i: Vec<f64> = Vec::new();

        let input = fs::read_to_string("input.txt").unwrap();

        for line in input.split(";") {
            i.push(line.parse::<f64>().unwrap());
        }

        let result: &f64 = nn.calc(&i).first().unwrap();

        println!("Result: {}", result);

        fs::write("result.txt", format!("{}", result)).unwrap();

}