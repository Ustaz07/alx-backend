import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(value);
  });
};

// Set the value of 'Holberton' to 'School'
setNewSchool('Holberton', 'School');

// Display the value for 'Holberton'
displaySchoolValue('Holberton');

// Set a new school and display its value
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
