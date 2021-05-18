use rand::{Rng, thread_rng};
use rand::distributions::{Uniform, Distribution};
use statrs::distribution::{Normal, Poisson};
use plotters::prelude::*;

fn generate_component() -> ((i32, i32),(i32, i32)) {

    let mut rng = thread_rng();

    let mut w = 0;
    let mut l = 0;
    loop {
        let g = Normal::new(50., 25.).unwrap();
        w = g.sample(&mut rng) as i32;
        l = g.sample(&mut rng) as i32;

        if w > 0 && l > 0 {
            break;
        }
    }

    let u = Uniform::new(0.0, 500.0);
    let x = rng.sample(u) as i32;
    let y = rng.sample(u) as i32;

    let ret = ((x - w/2, y - l/2), (x + w/2, y + l/2));
    //println!("{}, {}, {}, {}", ret.0.0, ret.0.1, ret.1.0, ret.1.1);
    //println!("/// {}", (ret.1.0 - ret.0.0));
    //println!("// {}", (ret.1.1 - ret.0.1));
    ret
}

fn intersect_component(c1: &((i32, i32),(i32, i32)),
                       c2: &((i32, i32),(i32, i32)),) -> bool {

    let mut points = Vec::new();
    points.push((c1.0.0, c1.0.1));
    points.push((c1.0.0, c1.1.1));
    points.push((c1.1.0, c1.1.1));
    points.push((c1.1.0, c1.0.1));

    let mut com_points = Vec::new();
    com_points.push((c2.0.0, c2.0.1));
    com_points.push((c2.0.0, c2.1.1));
    com_points.push((c2.1.0, c2.1.1));
    com_points.push((c2.1.0, c2.0.1));

    for i in 0..4 {
        if (points[i].0 >= c2.0.0 && points[i].0 <= c2.1.0 ) && (points[i].1 >= c2.0.1 && points[i].1 <= c2.1.1) {
            return true
        }
    }

    for i in 0..4 {
        if (com_points[i].0 >= c1.0.0 && com_points[i].0 <= c1.1.0 ) && (com_points[i].1 >= c1.0.1 && com_points[i].1 <= c1.1.1) {
            return true
        }
    }

    if c1.0.0 >= c2.0.0 && c1.0.0 <= c2.1.0 && c1.0.1 <= c2.0.1 && c1.1.1 >= c2.1.1 {
        return true
    }
    if c1.1.0 >= c2.0.0 && c1.1.0 <= c2.1.0 && c1.0.1 <= c2.0.1 && c1.1.1 >= c2.1.1 {
        return true
    }
    if c1.0.1 >= c2.0.1 && c1.0.1 <= c2.1.1 && c1.0.0 <= c2.0.0 && c1.1.0 >= c2.1.0 {
        return true
    }
    if c1.1.1 >= c2.1.1 && c1.0.1 <= c2.1.1 && c1.0.0 <= c2.0.0 && c1.1.0 >= c2.1.0 {
        return true
    }

    false
    
}

fn is_invalid_component(new_component: &((i32, i32),(i32, i32)),
                        components: &Vec<((i32, i32),(i32, i32))>) -> bool {

    if (((new_component.0.0 - new_component.1.0) >= -2)
        && ((new_component.0.0 - new_component.1.0) <= 2))
        || (((new_component.0.1 - new_component.1.1) >= -2)
        && ((new_component.0.1 - new_component.1.1) <= 2)) {
        return true;
    }

    if new_component.0.0 < 0 || new_component.0.1 < 0 || new_component.1.0 < 0 || new_component.1.1 < 0 {
        return true;
    }
    if new_component.0.0 > 500 || new_component.0.1 > 500 || new_component.1.0 > 500 || new_component.1.1 > 500 {
        return true;
    }

    for item in components.iter() {

        if intersect_component(item, new_component) {
            return true
        }
    }
    
    false
}

fn generate_pad(comp: &((i32, i32),(i32, i32)), lamb: f64) -> Vec<(i32, i32)> {
    let mut rng = thread_rng();
    let n = Poisson::new(lamb).unwrap();

    //println!("///  {}", n.sample(&mut rng));
    //println!("{}", (comp.1.0 - comp.0.0));
    //println!("{}", (comp.1.1 - comp.0.1));

    //let pads = (n.sample(&mut rng))*((comp.1.0 - comp.0.0) as f64)*((comp.1.1 - comp.0.1) as f64)/1000.0;
    let pads = (n.sample(&mut rng))*((comp.1.1 - comp.0.1) as f64)/100.;
    let mut pads = pads.floor() as i32;

    if pads <= 1 {
        pads = 2;
    }
    //println!("#pads {}", pads);

    let mut ret = Vec::new();
    let pad_step = (comp.1.1 - comp.0.1)*2/pads;
    //println!("{}", pad_step);
    for i in 0..pads {
        if i > pads/2 {
            ret.push((comp.1.0, comp.1.1 - (i-pads/2)*pad_step));
        } else {
            ret.push((comp.0.0, comp.0.1 + i*pad_step));
        }
    }
    //println!("{:?}", ret);

    ret
}

fn connect(pads) {
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Create a 800*600 bitmap and start drawing
    let mut backend = BitMapBackend::new("plotters-doc-data/1.png", (500, 500));
    backend.draw_rect((0,0), (500, 500), &WHITE, true)?;

    let mut components = Vec::new();
    for nc in 0..50 {
        let component = generate_component();
        if is_invalid_component(&component, &components) {
            continue;
        } else {
            backend.draw_rect(component.0, component.1, &RED, false)?;
            components.push(component);
        }
    }

    let mut pads = Vec::new();
    for comp in &components {
        let mut new_pads = generate_pad(comp, 12.);
        pads.append(&mut new_pads);
    }
    for p in pads {
        backend.draw_circle(p, 2, &GREEN, true)?;
    }

    let trace = connect(pads);

    Ok(())
}


