import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) => {
    const formattedResults = [];
    results.forEach((result) => {
      if (result.status === 'fulfilled') {
        formattedResults.push({
          status: result.status,
          value: result.value,
        });
      } else {
        formattedResults.push({
          status: result.status,
          value: String(result.reason),
        });
      }
    });
    return formattedResults;
  });
}
