// const span=document.getElementById("span");
// 
// const canvas = document.getElementById('Canvas');
// const ctx = canvas.getContext("2d");
// const img = document.getElementById("img");

// img.onload = resize(img)

// function resize(k) {
//     ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height); 
//     canvas.width = k.width; // destination canvas size
//     canvas.height = canvas.width * k.height / k.width;
 
//     var cur = {
//       width: Math.floor(k.width * 0.5),
//       height: Math.floor(k.height * 0.5)
//     }
 
//     oc.width = cur.width;
//     oc.height = cur.height;
 
//     // octx.drawImage(k, 0, 0, cur.width, cur.height);
 
//     // while (cur.width * 0.5 > k.width) {
//     //   cur = {
//     //     width: Math.floor(cur.width * 0.5),
//     //     height: Math.floor(cur.height * 0.5)
//     //   };
//     //   octx.drawImage(oc, 0, 0, cur.width * 2, cur.height * 2, 0, 0, cur.width, cur.height);
//     // }
 
//     // ctx.drawImage(oc, 0, 0, cur.width, cur.height, 0, 0, canvas.width, canvas.height);
//  }

// let lastKnownScrollPosition = 0;
// let imgs=[];

// for (let i = 1; i <= 111; i++) {
//   let ns;

//   if (i < 10) {
//       ns = "00" + String(i);
//   } else if (i < 100) {
//       ns = "0" + String(i);
//   } else {
//       ns = String(i);
//   }
//   let src = `ezgif-3-755ef763d8-png-split\\ezgif-frame-${ns}.png`;
//   let img=document.createElement("img")
//   img.scr=src
//   imgs.push(img)
// }

// resize(imgs[106])

// // function doSomething(scrollPos) {
// //   perch=(Math.ceil(((scrollPos/mv)*110)))+1;
// //   span.innerHTML=`Scroll=${perch}`;
// //   if (perch<10) {
// //     img.src=`ezgif-3-755ef763d8-png-split\\ezgif-frame-00${perch}.png`;
// //   }
// //   if (perch>=10) {
// //     img.src=`ezgif-3-755ef763d8-png-split\\ezgif-frame-0${perch}.png`;
// //   }
// //   if (perch>=100) {
// //     img.src=`ezgif-3-755ef763d8-png-split\\ezgif-frame-${perch}.png`;
// //   }
// // }


