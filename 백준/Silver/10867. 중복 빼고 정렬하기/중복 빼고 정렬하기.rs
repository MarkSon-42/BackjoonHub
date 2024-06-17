use std::collections::HashSet;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines().map(|l| l.unwrap());
    let _n: usize = lines.next().unwrap().parse().unwrap();
    let nums: HashSet<i32> = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(|num| num.parse().unwrap())
        .collect();
    let mut nums: Vec<i32> = nums.into_iter().collect();
    nums.sort();
    for num in nums {
        print!("{} ", num);
    }
}