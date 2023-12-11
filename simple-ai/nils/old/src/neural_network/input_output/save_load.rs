
use std::fs::File;
use std::path::PathBuf;
use std::io::{self, Error};
use std::io::prelude::*;

use crate::neural_network::NeuralNetwork;

pub fn save(name: PathBuf, to_save: &NeuralNetwork) -> io::Result<()> {
    let mut file: File = match File::open(&name) {
        Ok(f) => f,
        Err(_) => File::create(&name)?
    };
    let mut data = String::new();

    for (i, layer) in to_save.get_bias().iter().enumerate() {
        if i != 0 {data.push('|');}
        for (n, neuron) in layer.iter().enumerate() {
            if n != 0 {data.push(',');}
            data.push_str(&neuron.to_string());
        }
    }
    data.push('§');

    for (i, layer) in to_save.get_weight().iter().enumerate() {
        if i != 0 {data.push('|');}
        for (n, neuron) in layer.iter().enumerate() {
            if n != 0 {data.push(',');}
            for (c, connection) in neuron.iter().enumerate() {
                if c != 0 {data.push('~');}
                data.push_str(&connection.to_string());
            } 
        }
    }
    let result = file.write_all(data.as_bytes());
    result
}

pub fn load(path: PathBuf) -> io::Result<(Vec<Vec<f32>>, Vec<Vec<Vec<f32>>>)> {
    let mut bias: Vec<Vec<f32>> = Vec::new();
    let mut weight: Vec<Vec<Vec<f32>>> = Vec::new();
    let mut file = File::open(path)?;
    let mut buf = String::new();
    file.read_to_string(&mut buf)?;

    let mut data = buf.split('§');

    let bias_input = data.next().ok_or(Error::new(io::ErrorKind::Other, "the selected file dose not contains a NeuralNetwork"))?;    
    let weight_input = data.next().ok_or(Error::new(io::ErrorKind::Other, "the selected file dose not contains a NeuralNetwork"))?;

    for (i, layer) in bias_input.split('|').enumerate() {
        bias.push(Vec::new());
        for neuron in layer.split(',') {
            bias[i].push(match neuron.parse::<f32>()  {
                Ok(b) => b,
                Err(_) => return Err(Error::new(io::ErrorKind::Other, "Was not able to load the bias of the neurons"))
            });
        }
    }

    for (i, layer) in weight_input.trim().split('|').enumerate() {
        weight.push(Vec::new());
        for (n, neuron) in layer.split(',').enumerate() {
            weight[i].push(Vec::new());
            for connection in neuron.split('~') {
                weight[i][n].push(match connection.parse::<f32>()  {
                    Ok(b) => b,
                    Err(_) => return Err(Error::new(io::ErrorKind::Other, "Was not able to load the weight of the neurons"))
                });
            }
        }
    }

    Ok((bias, weight))
}

