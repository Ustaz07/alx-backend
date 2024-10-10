import kue from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((job) => {
    const jobData = queue.create('push_notification_code_3', job).save((err) => {
      if (!err) {
        console.log(`Notification job created: ${jobData.id}`);
      }
    });

    jobData.on('complete', () => {
      console.log(`Notification job ${jobData.id} completed`);
    })
    .on('failed', (error) => {
      console.log(`Notification job ${jobData.id} failed: ${error}`);
    })
    .on('progress', (progress) => {
      console.log(`Notification job ${jobData.id} ${progress}% complete`);
    });
  });
};

export default createPushNotificationsJobs;
