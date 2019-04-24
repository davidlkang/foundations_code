function main(repetitions, string) {
    var repeatedString = '';
    for(; repetitions > 0; repetitions--) {
        repeatedString += string;
    }
    return repeatedString
}

console.log(main(4, 'HelloWorld'));
