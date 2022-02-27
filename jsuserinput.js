let data = process.stdin.on('data', (data) => {
  return data.toString();
});
console.log(data);
