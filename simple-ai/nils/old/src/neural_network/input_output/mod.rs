use std::io::{self, Error};
use std::path::PathBuf;
use std::str::FromStr;

pub mod save_load;

pub enum Commands {
    Load(PathBuf),
    New(Vec<u32>),
    Exit,
    Save(PathBuf),
    Thinkm(Vec<f32>),
}

pub fn commandinput() -> io::Result<Commands> {
    let mut s = String::new();
    io::stdin().read_line(&mut s)?;
    let bind = s.trim().to_lowercase();
    let mut  siter = bind.as_str().split_whitespace();
    match siter.next() {
        Some("load") => return Ok(Commands::Load(PathBuf::from(siter.next().ok_or(Error::new(io::ErrorKind::InvalidInput, "Not enough arguments!"))?))),
        Some("save") => return Ok(Commands::Save(PathBuf::from(siter.next().ok_or(Error::new(io::ErrorKind::InvalidInput, "Not enough arguments!"))?))),
        Some("exit") => return Ok(Commands::Exit),
        Some("new") => return Ok(Commands::New(str_to_vec(siter.next().ok_or(Error::new(io::ErrorKind::InvalidInput, "Not enough arguments!"))?)?)),
        Some("thinkm") => return Ok(Commands::Thinkm(str_to_vec(siter.next().ok_or(Error::new(io::ErrorKind::InvalidInput, "Not enough arguments!"))?)?)),
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



