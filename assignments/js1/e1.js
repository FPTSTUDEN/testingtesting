'use strict';
//1 - 1pt
console.log("I'm printing to console!")
//2 - 2pts
let username=prompt("Enter your name:");
document.querySelector('.e2').innerHTML=`Hello, ${username}! Welcome to our website.`
//3 - 3pts
let i1=prompt("Int 1: ")
let i2=prompt("Int 2: ")
let i3=prompt("Int 3: ")
document.querySelector('.e3').innerHTML=`The sum is: ${parseInt(i1)+parseInt(i2)+parseInt(i3)}; The product is: ${parseInt(i1)*parseInt(i2)*parseInt(i3)}; The average is: ${(parseInt(i1)+parseInt(i2)+parseInt(i3))/3}`
//4 - 3pts
let student_name=prompt("Enter your name: ")
let val=Math.floor(Math.random()*4)+1 //1-4
switch(val){
    case 1:
        var house="Gryffindor"
        break;
    case 2:
        var house="Hufflepuff"
        break;
    case 3:
        var house="Ravenclaw"
        break;
    case 4:
        var house="Slytherin"
        break;
}
document.querySelector('.e4').innerHTML=`${student_name}, you are ${house}!`
//5 - 3pts
let year=prompt("Enter a year: ")
if((year%4==0 && year%100!=0) || (year%400==0)){
    document.querySelector('.e5').innerHTML=`${year} is a leap year.`
}else{
    document.querySelector('.e5').innerHTML=`${year} is not a leap year.`
}
//6 - 3pts
let answer=confirm("Should I calculate the square root?")
if(answer){
    let number=prompt("Enter a number to find the square root of: ")
    document.querySelector('.e6').innerHTML=`The square root of ${number} is ${Math.sqrt(number)}`
} else{
    document.querySelector('.e6').innerHTML=`The square root is not calculated.`
}
//7 - 2pts
let dicenum=prompt("Enter the number of dice to roll: ")
let total=0
for(let i=0;i<dicenum;i++){
    total+=Math.floor(Math.random()*6)+1
}
document.querySelector('.e7').innerHTML=`Total roll is: ${total}`
//8
//9 - 2pts
let num=prompt("Enter a number to check if it's prime: ")
let isPrime=true
if (num<=1){
    isPrime=false
}
for(let i=2;i<=Math.sqrt(num);i++){
    if(num%i==0){
        isPrime=false
        break;
    }
}
if(isPrime){
    document.querySelector('.e9').innerHTML=`${num} is a prime number.`
}else{
    document.querySelector('.e9').innerHTML=`${num} is not a prime number.`
}
//total: 19pts