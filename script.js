const canvas=document.getElementById("Canvas");
const ctx=canvas.getContext("2d");
const mv=document.documentElement.offsetHeight-window.innerHeight;
let imgs=[];
let scrollis=false;

const span=document.getElementById("span")


for (let i = 1; i <= 111; i++) {
  let ns;

  if (i < 10) {
      ns = "00" + String(i);
  } else if (i < 100) {
      ns = "0" + String(i);
  } else {
      ns = String(i);
  }
  let ksrc = `ezgif-3-755ef763d8-png-split\\ezgif-frame-${ns}.png`;
  let img=document.createElement("img")
  img.src=ksrc
  imgs.push(img)
}

const ddata = {
  div1mn: 0,
  div1mx: 700,
  div2mn: 700,
  div2mx: 1400,
  div3mn: 1400,
  div3mx: 2100,
  div4mn: 2100,
  div4mx: 2800
}

function inRegion(lksp) {
  let c=[];
  if ((lksp>=0 && lksp<700)) {
    c.push(["div1", 0]);
  } else if (lksp+700>=0 && lksp+700<700) {
    c.push(["div1"], 1)
  };
  if ((lksp>=700 && lksp<1400)) {
    c.push(["div2", 0]);
  } else if (lksp+700>=700 && lksp+700<1400) {
    c.push(["div2", 1])
  };
  if ((lksp>=1400 && lksp<2100)) {
    c.push(["div3", 0]);
  } else if (lksp+700>=1400 && lksp+700<2100) {
    c.push(["div3", 1])
  };
  if ((lksp>=2100 && lksp<2800)) {
    c.push(["div4", 0]);
  } else if (lksp+700>=2100 && lksp+700<2800) {
    c.push(["div4", 1])
  };
  return c;
}

function hPer(lksp) {
  let divs=inRegion(lksp);
  let dic={};
  let s="";
  for (div in divs) {
    let x=divs[div][1];
    if (x==0) {
      o="mx"
    } else {
      o="mn"
    }
    let per=((700*x-(-1+2*x)*((ddata[`${divs[div][0]}`+o])-lksp))/700)*100
    dic[`${divs[div][0]}`]=per
    s=s+`${divs[div][0]} is ${per}%`+" ";
  };
  span.innerHTML=s;
  return dic
}

// function scrolle(i) {
//   window.scrollTo({
//     top: i,
//     behavior: "smooth"});
// };

// function stacks() {
  // const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
  // scrollis=true;
  // if ((lksp+100)<700) {(
  //   async () => {
  //     for (let i = 1; i<= 70; i++) {
  //       scrolle(350+5*i)
  //       await sleep(4);
  //     };
  //   })();
  //   console.log("noreverse");}
//   if ((lksp+100)>700) {(
//     async () => {
//       for (let i = 700; i>= 350; i=i-5) {
//         scrolle(i)
//         await sleep(4);
//       };
//     })();
//     console.log("reverse");}
// }

imgs[0].onload= () => {
    ctx.drawImage(imgs[0], 0, 0, 300, 300);
}

function scrolling(lksp, sat) {
  let dils=null;
  if (sat==false) {
    dils=hPer(lksp);
  } else {
    dils=hPer(window.scrollY);
  }
  if (((50>Object.values(dils)[0] && Object.values(dils)[0]>40) || (50>Object.values(dils)[1] && Object.values(dils)[1]>40)) && sat==false) {
    console.log("fire")
    setTimeout(() => {
      scrolling(lksp, true);
    }, 1000);
  }
  if (((50>Object.values(dils)[0] && Object.values(dils)[0]>40) || (50>Object.values(dils)[1] && Object.values(dils)[1]>40)) && sat) {
    if (Object.values(dils)[0] > Object.values(dils)[1]) {
      e=document.getElementById(Object.keys(dils)[0]);
      e.scrollIntoView({ behavior: "smooth", block: "start", inline: "nearest" });
      console.log("scrolled")
    } 
    if (Object.values(dils)[0] > Object.values(dils)[1]) {
      e=document.getElementById(Object.keys(dils)[1]);
      e.scrollIntoView({ behavior: "smooth", block: "start", inline: "nearest" });
      console.log("scrolled")
    }
  }
}

document.addEventListener("scroll", (event) => {
    let lksp1 = window.scrollY;
    scrolling(lksp1, false)
    doSomething(lksp1);
  });

function doSomething(lksp) {
  perch=(Math.ceil(((lksp/mv)*110)))+1;
  ctx.drawImage(imgs[perch], 0, 0, 300, 300);
}


