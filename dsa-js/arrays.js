const strings = ['a', 'b', 'c', 'd'];
strings.push('e');
console.log(strings);
strings.pop();

// unshift, add element at the beginning
strings.unshift('x');

// splice, at position 2 delete 0 element, and add 'alien' at position 2
strings.splice(2, 0, 'alien');
