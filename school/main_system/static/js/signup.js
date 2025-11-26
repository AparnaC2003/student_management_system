// enabling submit button only if all fields are filled
document.getElementById("username").addEventListener("input",checkform);
document.getElementById("email").addEventListener("input",checkform);
document.getElementById("role").addEventListener("change",checkform);
document.getElementById("password").addEventListener("input",checkform);
document.getElementById("repass").addEventListener("input",checkform);

function checkform()
{
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("email").value.trim();
    const role = document.getElementById("role").value.trim();
    const password = document.getElementById("password").value.trim();
    const repass = document.getElementById("repass").value.trim();

    const button = document.querySelector("button[type='submit']");

    if(username === "" || email === "" || role === "" || password === "" || repass === "")
    {
        button.disabled = true;
    }
    else
    {
        button.disabled = false;
    }
}


//visible and invisible  password
function togglePassword(inputId,icon)
{
    const input = document.getElementById(inputId);
    if(input.type === 'password')
    {
        input.type = 'text';
        icon.classList.toggle("bx-show");   //if bx-show prnt remove it and vise versa
        icon.classList.toggle("bx-hide");   //if bx-hide prsnt remove it and vise versa
    }
    else
    {
        input.type = "password"
        icon.classList.toggle("bx-show");   //if bx-show prnt remove it and vise versa
        icon.classList.toggle("bx-hide");   //if bx-hide prsnt remove it and vise versa
    }
}

// password == repass ???

function validate_password()
{
    pass = document.getElementById("password");
    repa = document.getElementById("repass");
    if(pass.value != repa.value)
    {
        document.getElementById("incorrect").style.display = "block";
    }
    else
    {
        document.getElementById("incorrect").style.display = "none";
    }
}



