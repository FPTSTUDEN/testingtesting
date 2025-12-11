'use strict'; 
console.log('Script loaded successfully');
// document.querySelector(".site-logo").style.color = 'brown';


// const navLinks = document.querySelectorAll('.nav-links a');
// navLinks.forEach(link => {
//     link.style.fontWeight = 'bold';
// });
// const header = document.querySelector('.header');
// header.style.backgroundColor = '#f0f0f0';

document.querySelector(".target").style.backgroundColor = 'yellow';

let username=prompt("Enter your name:");
alert(`Hello, ${username}! Welcome to our website.`);
let targetDiv = document.querySelector('.target');
targetDiv.innerHTML = `This content was added by JavaScript. Welcome, ${username}!`;
switch (username.toLowerCase()) {
    case 'alice':
        targetDiv.style.backgroundColor = 'lightblue';
        break;
    case 'bob':
        targetDiv.style.backgroundColor = 'lightgreen';
        break;
    default:
        targetDiv.style.backgroundColor = 'lightgray';
}