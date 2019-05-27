function reverseString(s:string):string {
    let char = Array.from(s);
    char = char.reverse();
    return char.join('');
}

console.log(reverseString('Jeff'));
