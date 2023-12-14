use std::fs::File;
use std::io::{self, Error, Read};
use std::path::PathBuf;
use std::str::FromStr;

use neuroflow::data::DataSet;

pub enum Commands {
    Load(String),
    New(Vec<i32>),
    Exit,
    Save(String),
    Thinkm(Vec<f64>),
    LoadData(PathBuf),
    Learn((f64, i64))
}

pub fn commandinput() -> io::Result<Commands> {
    let mut s = String::new();
    io::stdin().read_line(&mut s)?;
    let bind = s.trim().to_lowercase();
    let mut  siter = bind.as_str().split_whitespace();
    match siter.next() {
        Some("load") => return Ok(Commands::Load(String::from(siter.next().ok_or(Error::new(io::ErrorKind::InvalidInput, "Not enough arguments!"))?))),
        Some("save") => return Ok(Commands::Save(String::from(siter.next().ok_or(Error::new(io::ErrorKind::InvalidInput, "Not enough arguments!"))?))),
        Some("exit") => return Ok(Commands::Exit),
        Some("new") => return Ok(Commands::New(str_to_vec(siter.next().ok_or(Error::new(io::ErrorKind::InvalidInput, "Not enough arguments!"))?)?)),
        Some("thinkm") => return Ok(Commands::Thinkm(str_to_vec(siter.next().ok_or(Error::new(io::ErrorKind::InvalidInput, "Not enough arguments!"))?)?)),
        Some("td") => return Ok(Commands::LoadData(PathBuf::from(siter.next().ok_or(Error::new(io::ErrorKind::InvalidInput, "Not enough arguments!"))?.trim()))),
        Some("learn") => return Ok(Commands::Learn((0.0001, 5000))),
        _ => return Err(Error::new(io::ErrorKind::InvalidInput, "This Command dose not exist!")),
    }
}

pub fn str_to_vec<T>(input: &str) -> io::Result<Vec<T>>
    where
        T: FromStr,
{
    let mut output: Vec<T> = Vec::new();

    for layer in input.trim().split("|") {
        output.push( match layer.parse::<T>() {
            Ok(i) => i,
            _ => return Err(Error::new(io::ErrorKind::InvalidInput, "Not a valid number!")),
        });
    }
    Ok(output)
}

pub fn load_data(path: PathBuf) -> io::Result<DataSet> {
    let mut data = DataSet::new();
    let mut file = File::open(path)?;
    let mut buf = String::new();
    file.read_to_string(&mut buf)?;

    let pain = buf.pop().ok_or(Error::new(io::ErrorKind::InvalidInput, "This file can not be used as trainings data: 05"))?;
    if pain != '§' {buf.push(pain)}

    for te in buf.split('§') {
        let mut dar = te.trim().split('|');

        let mut input: Vec<f64> = Vec::new();

        for dp in dar.next().ok_or(Error::new(io::ErrorKind::InvalidInput, "This file can not be used as trainings data: 01"))?.trim().replace(&['(', ')', ' '], "").split(',') {
            input.push(match dp.trim().parse::<f64>() {
                Ok(r) => r / 255.0 ,
                Err(_) => return Err(Error::new(io::ErrorKind::InvalidInput, "This file can not be used as trainings data: 02")),
            })
        }

        let er = match dar.next().ok_or(Error::new(io::ErrorKind::InvalidInput, "This file can not be used as trainings data: 03"))?.trim().parse::<f64>() {
            Ok(r) => vec![r],
            Err(_) => return Err(Error::new(io::ErrorKind::InvalidInput, "This file can not be used as trainings data: 04")),
        };

        data.push(&input, &er)
    }

    return Ok(data);
}


