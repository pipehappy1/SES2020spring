use rand::{Rng, thread_rng};
use rand::distributions::{Uniform, Distribution};
use statrs::distribution::Normal;
use plotters::prelude::*;

fn generate_component() -> ((i32, i32),(i32, i32)) {

    let mut rng = thread_rng();
    
    let g = Normal::new(50., 50.).unwrap();
    let w = g.sample(&mut rng) as i32;
    let l = g.sample(&mut rng) as i32;

    let u = Uniform::new(0.0, 500.0);
    let x = rng.sample(u) as i32;
    let y = rng.sample(u) as i32;

    let ret = ((x - w/2, y - l/2), (x + w/2, y + l/2));
    //println!("{}, {}, {}, {}", ret.0.0, ret.0.1, ret.1.0, ret.1.1);
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

    if new_component.0.0 == new_component.1.0 || new_component.0.1 == new_component.1.1 {
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


fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Create a 800*600 bitmap and start drawing
    let mut backend = BitMapBackend::new("plotters-doc-data/1.png", (500, 500));

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
    
    Ok(())
}


