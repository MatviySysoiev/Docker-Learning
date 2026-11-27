import fs from 'fs'

fs.appendFile('my-file.txt', 'File Node.js was created!', (err) => {
    if (err) throw err
    console.log('File was saved!')
})

setTimeout(() => console.log('End', 50000))