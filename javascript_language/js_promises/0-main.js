import addNumbers from './0-addNums';

addNumbers(5, 10)
    .then(result => {
        console.log('The sum is:', result); // Will log "The sum is: 15"
    })
    .catch(error => {
        console.error('Error:', error); // Will log an error if inputs are invalid
    });
