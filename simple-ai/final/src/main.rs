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

    let mut exit = false;
    let mut nn: FeedForward = FeedForward::new(&[1,1]);
    nn.activation(Tanh);
    let mut data = DataSet::new();
    
    nn = neuroflow::io::load("20231211_cai").unwrap();

    let listener = TcpListener::bind("127.0.0.1:3000").unwrap();

    for stream in listener.incoming() {
        let mut stream = stream.unwrap();

        let mut headers = [httparse::EMPTY_HEADER; 64];
        let mut req = httparse::Request::new(&mut headers);
    
        // let mut buf_reader = BufReader::new(&mut stream);
        // let http_request: Vec<_> = buf_reader
        //     .lines()
        //     .map(|result| result.unwrap())
        //     .take_while(|line| !line.is_empty())
        //     .collect();

        // println!("Request: {:#?}", http_request);

        // let mut buffer = [0; 1024];
        // stream.read(&mut buffer).unwrap();

        // println!("Request:");
        
        // let mut started_getting_values = false;

        // for line_str in  String::from_utf8_lossy(&buffer[..]).split("\n") {
            

        //     if line_str == "\n" {
        //         print!("Empty ");
        //     }

        //     let pattern = r"\\";
        //     let regex = Regex::new(pattern).unwrap();

        //     let escaped_string = regex.replace_all(&line_str, "\\\\").to_string();

        //     println!("|{}|", escaped_string);
        // }

        let i: Vec<f64> = vec![1.0, 1.0, 1.0];

        let result: &f64 = nn.calc(&i).first().unwrap();
        // for result in results {
        //     println!("{}", result);
        // }

        println!("Result: {}", result);

        let status_line = "HTTP/1.1 200 OK";
        let contents = "Hello World";
        let length = contents.len();

        let response =
            format!("{status_line}\r\nContent-Length: {length}\r\n\r\n{contents}");

        stream.write_all(response.as_bytes()).unwrap();
    }

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