"use strict"
// Q3
let num1 = 5, num2 = 10;
let output;
let num3 = 3;
output += "result: " + num1 + num3 * num2;

console.log(output);

// Q4
// Math.floor(Math.random()*-25); works
// Math.ceil(Math.random()*-25)-1; works
// Math.floor(Math.random()*-24)-1; cant work
/*let val = 0;
while (val != -1) {
    val = Math.ceil(Math.random()*-25)-1;
    console.log(val);
}*/
// wrong console.log(Math.floor(Math.random()*-25));
console.log(Math.ceil(Math.random()*-25)-1);

// Q5
let a = 1.5;
let b = 3.4;
let angleA = Math.atan(a/b)*180/Math.PI;
let angleB = Math.atan(b/a)*180/Math.PI;

console.log(`Angle A: ${angleA.toFixed(2)} Degrees, Angle B: ${angleB.toFixed(2)} Degrees.`);
// console.log("Angle A: " + A.toFixed(2) + " Degrees, Angle B: " + B.toFixed(2) +" Degrees.")
