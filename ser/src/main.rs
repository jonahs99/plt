use std::io::stdin;
use std::env;
use std::time::Duration;

use std::io::prelude::*;
use serial::prelude::*;

fn main() {
    let device = env::args_os().nth(1).unwrap();

    let mut port = serial::open(&device).unwrap();
    // port.set_timeout(Duration::from_millis(60000)).unwrap();
    port.set_timeout(Duration::from_millis(200)).unwrap();
    port.reconfigure(&|settings| {
        settings.set_flow_control(serial::FlowHardware);
        Ok(())
    }).unwrap();
    println!("opened");

    let mut line = String::new();
    while {line.clear(); stdin().read_line(&mut line).is_ok()} {
        println!("{}", &line);

        if !port.write(line.as_bytes()).is_ok() {
            let mut read = Vec::new();
            while port.read(&mut read).unwrap() > 0 { }
            println!("read {}", std::str::from_utf8(&read).unwrap());
            break;
        }

        /*
        let mut read = Vec::new();
        if port.read(&mut read).unwrap() > 0 {
            println!("read {}", std::str::from_utf8(&read).unwrap());
        }
        */
    }
}

