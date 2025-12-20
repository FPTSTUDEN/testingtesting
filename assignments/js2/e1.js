'use strict';
//1 - 2pt
let numlist = [];
for (let i = 1; i <= 5; i++) {
    let num = prompt(`1. Enter number ${i}:`);
    numlist.push(parseFloat(num));
}
for (let i = 5; i >= 1; i--) {
    console.log(numlist[i - 1]); //print in reverse order
}
//2 - 2pts
let participant_count=prompt("2. Enter number of participants: ")
let greeting_list=[]
for (let i=1;i<=participant_count;i++){
    let name=prompt(`2. Enter the name of participant ${i}: `)
    greeting_list.push(name)
}
greeting_list.sort() //alphabetical order
let list_content="<ol>"
for (let i=0;i<participant_count;i++){
    list_content+=`<li>${greeting_list[i]}</li>`
    // list_content+=`<li>Hello, ${greeting_list[i]}! Welcome to the event.</li>`
}
list_content+="</ol>"
document.querySelector('.e2').innerHTML=list_content

//3 - 2pts
let dog_list=[]
for (let i=1;i<=6;i++) {
    dog_list.push(prompt(`3. Name of dog ${i}: `))
}
dog_list.sort().reverse()
list_content="<ul>"
for (let i=0;i<6;i++){
    list_content+=`<li>${dog_list[i]}</li>`
}
list_content+="</ul>"
document.querySelector('.e3').innerHTML=list_content
//4 - 2pts
numlist=[]
let num=parseFloat(prompt("4. Enter a number: "))
while (num!=0) {
    numlist.push(num)
    num=parseFloat(prompt("4. Enter a number: "))
}
console.log("You entered 0! Operation stopped.")
numlist.sort((a,b)=>b-a) //reversed
for (const element of numlist) {
    console.log(element);
}
//5 - 2pts
numlist=[]
num=parseFloat(prompt("5. Enter a number: "))
while (!numlist.includes(num)) {
    numlist.push(num)
    num=parseFloat(prompt("5. Enter a number: "))
}
console.log("Number already included! Operation stopped.")
numlist.sort((a,b)=>a-b) //asc
for (const element of numlist) {
    console.log(element);
}
//6 - 2pts

list_content="<ul>"
let roll=Math.floor(Math.random()*6)+1
while (roll!=6){
    list_content+=`<li>Rolled a ${roll}</li>`
    roll=Math.floor(Math.random()*6)+1 //new roll
}
list_content+=`<li>Done. Rolled a 6</li>`
list_content+="</ul>"
document.querySelector('.e6').innerHTML=list_content
//7 - 2pts
list_content="<ul>"
let sides=parseFloat(prompt("7. Number of dice sides: "))
roll=Math.floor(Math.random()*sides)+1
while (roll!=sides){
    list_content+=`<li>Rolled a ${roll}</li>`
    roll=Math.floor(Math.random()*sides)+1
}
list_content+=`<li>Done. Rolled a ${sides}</li>`
list_content+="</ul>"
document.querySelector('.e7').innerHTML=list_content
//8 - 2pts
function concat(array) {
    let res=""
    for (const element of array) {
        res+=element;
    }
    return res //return concatenated string
}
document.querySelector('.e8').innerHTML=concat(["a","b","c"])
//9 - 2pts
function even(array) {
    return array.filter(num => num%2===0); //return new array with even numbers only
}
numlist=[1,2,3,4,5,6]
let evenlist=even(numlist)
console.log(numlist)
console.log(evenlist)

//total:  18pts