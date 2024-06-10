function solution(tickets) {
    let routes = {};

    for(let i=0; i<tickets.length; i++) {
        const [from, to] = tickets[i];
        if(routes[from]) {
            routes[from].push(to);
        } else {
            routes[from] = [to];
        }
    }

    for(let route in routes) {
        routes[route].sort().reverse();
    }

    let stack = ["ICN"];
    let path = [];

    while(stack.length > 0) {
        let top = stack[stack.length - 1];

        if(routes[top] && routes[top].length > 0) {
            stack.push(routes[top].pop());
        } else {
            path.unshift(stack.pop());
        }
    }

    return path;
}