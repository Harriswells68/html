const yes = document.getElementById("yes");

yes.addEventListener("click", () => {
    fetch("http://localhost:8080/question")
        .then(response => {
            console.log(response)
            response.json()
        })
        .then(data => {
            console.log(data); // Logs the JSON data
            // Update the DOM with the received data
            const questionElement = document.getElementById('question');
            questionElement.innerHTML = "${data}"; // Display the question
        })
        .catch(error => console.error('Fetch error:', error));
});