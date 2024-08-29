const b1=document.getElementById("kki");
const w = window.innerWidth;
const h = window.innerHeight; 

b1.addEventListener("mouseover", function callchange(e) {
    changego(e);
});

function changego(e) {
    e.target.style.position = "absolute";
    e.target.style.left=`${getRandomInt(0, w)}`+'px';
    e.target.style.top=`${getRandomInt(0, h)}`+'px';
}

function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled); // The maximum is exclusive and the minimum is inclusive
  }  
// function primeNumber() {
//     let num1=parseInt(prompt("Enter The Lower Range: "), 10);
//     let num2=parseInt(prompt("Enter The Upper Range: "), 10);
//     for(let i=num1; i<=num2; i++) {
//         let k=0;
//         for(let j=2; j<i; j++) {
//             if (i%j==0) {
//                 k=1
//             };
//         };
//         if (k==0) {
//             document.querySelector("pre").innerText=document.querySelector("pre").innerText+`The Number ${i} is Prime`+"\n";
//         } else {
//             document.querySelector("pre").innerText=document.querySelector("pre").innerText+`The Number ${i} is Not Prime`+"\n";
//         };
//     };
// }
