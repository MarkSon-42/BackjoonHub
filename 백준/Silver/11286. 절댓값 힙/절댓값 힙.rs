// rust 연습용으로 찍어봄. 아직 난이도를 더 낮춰야 할듯..

use std::collections::BinaryHeap;
use std::cmp::Ordering;
use std::io::{self, BufRead};

#[derive(Eq, PartialEq)]
struct AbsHeapVal(i32, i32);

impl Ord for AbsHeapVal {
    fn cmp(&self, other: &Self) -> Ordering {
        self.0.cmp(&other.0)
            .then_with(|| self.1.cmp(&other.1))
            .reverse()
    }
}

impl PartialOrd for AbsHeapVal {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

struct AbsHeap(BinaryHeap<AbsHeapVal>);

impl AbsHeap {
    fn new() -> Self {
        AbsHeap(BinaryHeap::new())
    }

    fn push(&mut self, x: i32) {
        self.0.push(AbsHeapVal(x.abs(), x));
    }

    fn pop(&mut self) -> Option<i32> {
        self.0.pop().map(|val| val.1)
    }
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let n: usize = lines.next().unwrap().unwrap().parse().unwrap();
    let mut heap = AbsHeap::new();

    for _ in 0..n {
        let x: i32 = lines.next().unwrap().unwrap().parse().unwrap();
        if x == 0 {
            println!("{}", heap.pop().unwrap_or(0));
        } else {
            heap.push(x);
        }
    }
}