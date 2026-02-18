function validate(e) {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const pass = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const msgbox = document.getElementById("msgbox");

    let msg = "";
    if (email === "") {
        msg += "Please enter an E-mail. ";
        msgbox.style.color = "red";
    } else if (pass === "") {
        msg += "Please enter a password. ";
        msgbox.style.color = "red";
    } else if (age === "") {
        msg += "Please enter your age. ";
        msgbox.style.color = "red";
    } else {
        msg += "Login successful!";
        msgbox.style.color = "green";
    }
    msgbox.innerHTML = message;
    document.getElementById("LoginForm").onsubmit = validate;

    document.getElementById("email").oninput = () => validate({preventDefault: () => {}});
    document.getElementById("password").oninput = () => validate({preventDefault: () => {}});;
    document.getElementById("age").oninput = () => validate({preventDefault: () => {}});
}