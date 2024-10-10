const redis = require('redis');

// Create Redis client
const client = redis.createClient();

// Connect to Redis server
client.on('connect', () => {
    console.log('Connected to Redis...');
});

// Set and Get example
client.set('framework', 'Express', (err, reply) => {
    if (err) throw err;
    console.log(reply); // OK
});

client.get('framework', (err, reply) => {
    if (err) throw err;
    console.log(reply); // Express
});
