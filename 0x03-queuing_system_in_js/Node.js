client.hmset('user:1000', {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25
}, (err, reply) => {
    if (err) throw err;
    console.log(reply); // OK
});

client.hgetall('user:1000', (err, obj) => {
    if (err) throw err;
    console.log(obj);
});
