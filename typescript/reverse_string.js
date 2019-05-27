function reverseString(s) {
    var char = Array.from(s);
    char = char.reverse();
    return char.join('');
}
console.log(reverseString('Jeff'));
