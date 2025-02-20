document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const terms = document.getElementById('terms').checked;


    if (!firstName || !lastName || !email || !password || !terms) {
        alert("გთხოვთ, შეავსოთ ყველა ველი");
    } else {
        console.log( firstName);
        console.log( lastName);
        console.log( email);
        console.log(password)
        console.log;
    }
});
