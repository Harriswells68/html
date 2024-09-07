var qn=1;
const no=document.getElementById("no");
const yes = document.getElementById("yes");

yes.addEventListener("click", () => {
    const url = "https://fuzzy-spork-jx646p6qx9v3pvg7-5000.app.github.dev/answer";
    fetch(url, {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify({[qn]:"yes"}),
    })
    .then(response => response.json())
    .then(data => changeQuestion(data))
  })

no.addEventListener("click", () => {
    const url = "https://fuzzy-spork-jx646p6qx9v3pvg7-5000.app.github.dev/answer";
    fetch(url, {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify({[qn]:"no"}),
    })
    .then(response => response.json())
    .then(data => changeQuestion(data))
  })

function changeQuestion(data) {
    qn=qn+1
    document.getElementById('question').innerText=Object.values(data)[0]
};