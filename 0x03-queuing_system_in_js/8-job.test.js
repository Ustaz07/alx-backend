import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  before(() => {
    // Create a new queue instance
    queue = kue.createQueue();

    // Mock the testMode functionality
    queue.testMode = {
      jobs: [],
      create: (data) => {
        const job = { data };
        queue.testMode.jobs.push(job);
        return job;
      },
      clear: () => {
        queue.testMode.jobs.length = 0; // Clear the mock jobs
      },
    };
  });

  // Clear the jobs array after each test
  afterEach(() => {
    queue.testMode.clear(); // Clear the queue after each test
  });

  after(() => {
    queue.testMode = false; // Exit test mode after all tests
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs when valid jobs are provided', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate the jobs in the queue
    const queuedJobs = queue.testMode.jobs; // Access the jobs array directly
    expect(queuedJobs.length).to.equal(2);
    expect(queuedJobs[0].data).to.deep.equal(jobs[0]);
    expect(queuedJobs[1].data).to.deep.equal(jobs[1]);
  });

  it('should not create jobs if jobs is an empty array', () => {
    const jobs = [];
    createPushNotificationsJobs(jobs, queue);
    
    // Validate the jobs in the queue
    const queuedJobs = queue.testMode.jobs; // Access the jobs array directly
    expect(queuedJobs.length).to.equal(0);
  });

  it('should create only jobs with valid structure', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is a test message' },
      { phoneNumber: '4153518781', message: 'This is another test message' },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate the jobs
    const queuedJobs = queue.testMode.jobs; // Access the jobs array directly
    expect(queuedJobs.length).to.equal(2);
    expect(queuedJobs.every(job => job.data.phoneNumber && job.data.message)).to.be.true;
  });
});
