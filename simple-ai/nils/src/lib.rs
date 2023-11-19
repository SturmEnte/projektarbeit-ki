
use std::io;
use neural_network::input_output::{commandinput, Commands};
use neural_network::NeuralNetwork;

pub fn run() -> io::Result<()> {
    let mut exit = false;
    let mut neural_network = NeuralNetwork::new(vec![1, 1]);
    while exit == false {
        match commandinput() {
            Ok(Commands::Load(p)) => match neural_network::input_output::save_load::load(p) {
                Ok(n) => neural_network = NeuralNetwork::load(n.0, n.1),
                Err(e) => eprintln!("Loading faild: {}", e),
            },
            Ok(Commands::Thinkm(i)) => match neural_network.think(i) {
                Ok(e) => for n in e {
                    println!("{}", n);
                },
                Err(e) => eprintln!("{}", e),
            },
            Ok(Commands::Exit) => exit = true,
            Ok(Commands::Save(p)) => neural_network::input_output::save_load::save(p, &neural_network)?,
            Ok(Commands::New(i)) => neural_network = NeuralNetwork::new(i),
            Err(e) if e.kind() == io::ErrorKind::InvalidInput => eprintln!("{}", e),
            Err(e) => return Err(e)
        }
    }
    return Ok(());
}

pub mod neural_network {
    use rand::random;
    use std::io::{self, Error};

    pub mod input_output;

    pub struct NeuralNetwork {
        bias: Vec<Vec<f32>>, 
        weight: Vec<Vec<Vec<f32>>>,
    }

    impl NeuralNetwork {
        pub fn new(number_nurons: Vec<u32>) -> Self {
            let mut weight: Vec<Vec<Vec<f32>>> = Vec::new();
            let mut bias: Vec<Vec<f32>> = Vec::new();
            let mut previous_layer: Option<u32> = None;

            for (val, n) in number_nurons.iter().enumerate() {
                if let Some(pn) = previous_layer {
                    bias.push(Vec::new());
                    weight.push(Vec::new());
                    for nc in 0..*n {
                        bias[val - 1].push(random::<f32>());

                        weight[val - 1].push(Vec::new());
                        for _ in 0..pn {
                            weight[val - 1][usize::try_from(nc).expect("What have you done?")].push(random::<f32>());
                        }
                    }

                }
                previous_layer = Some(*n);
            }

            NeuralNetwork {bias: bias, weight: weight}
        }


        pub fn load(bias: Vec<Vec<f32>>, weight: Vec<Vec<Vec<f32>>>) -> Self {
            NeuralNetwork {bias: bias, weight: weight}
        }

        pub fn get_bias(&self) -> &Vec<Vec<f32>> {
            &self.bias
        }

        pub fn get_weight(&self) -> &Vec<Vec<Vec<f32>>> {
            &self.weight
        }

        pub fn think(&self, input: Vec<f32>) -> io::Result<Vec<f32>> {
            for n in &input {
                if *n > 1.0 || *n < -1.0 {return Err(Error::new(io::ErrorKind::InvalidData, "Numbers have to be between 1 and -1"));}
            }
            let mut layer1 = input;

            for (layer_number, layer) in self.weight.iter().enumerate() {
                let mut layer2: Vec<f32> = Vec::new();
                for (neuron_number, neuron) in layer.iter().enumerate() {
                    let mut neuron_activation: f32 = 0.0;
                    for (c, connection) in neuron.iter().enumerate() {
                        neuron_activation += connection * layer1[c];
                    }
                    neuron_activation = (neuron_activation + self.bias[layer_number][neuron_number]) * -1.0;
                    layer2.push(1.0 / (1.0 + std::f32::consts::E.powf(neuron_activation)));
                }
                layer1 = layer2;
            }
            Ok(layer1)
        }
    }   

}


