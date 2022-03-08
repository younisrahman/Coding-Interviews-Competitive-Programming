const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question('Enter a number: ', (number) => {
  console.log(primecheck(number));
  readline.close();
});

const primecheck = (number) => {
  if (number <= 2) {
    return true;
  }
  for (let i = 2; i < number; i++) {
    if (number % i == 0) {
      return false;
    }
  }
  return true;
};
