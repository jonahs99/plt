use clap::Parser;
use serial::prelude::*;
use std::io::prelude::*;
use std::io::stdin;
use std::io::BufReader;
use std::time::Duration;

#[derive(Parser)]
struct Opts {
    /// Device to stream to
    #[clap()]
    device: String,
    /// For arduino based hardware, wait for ok messages
    #[clap(short, long)]
    pong: bool,
}

fn main() {
    let opts = Opts::parse();
    stream(opts);
}

fn stream(opts: Opts) {
    let mut port = serial::open(&opts.device).unwrap();
    port.set_timeout(Duration::from_millis(60000)).unwrap();

    port.reconfigure(&|settings| {
        settings.set_flow_control(serial::FlowHardware);
        Ok(())
    })
    .unwrap();
    println!("opened");

    let mut line = String::new();
    while let Ok(n_read) = {
        line.clear();
        stdin().read_line(&mut line)
    } {
        if n_read == 0 {
            // end of file
            break;
        }

        println!("{}", &line);

        if line.starts_with(';') {
            continue;
        }

        if !port.write(line.as_bytes()).is_ok() {
            let mut read = Vec::new();
            while port.read(&mut read).unwrap() > 0 {}
            println!("read {}", std::str::from_utf8(&read).unwrap());
            break;
        }

        if opts.pong {
            port = wait_for_ok(port);
        }
    }
}

fn wait_for_ok(port: serial::SystemPort) -> serial::SystemPort {
    let mut reader = BufReader::new(port);
    let mut line = String::new();
    loop {
        line.clear();
        reader.read_line(&mut line).unwrap();
        if line.starts_with("ok") {
            break;
        }
    }
    reader.into_inner()
}
