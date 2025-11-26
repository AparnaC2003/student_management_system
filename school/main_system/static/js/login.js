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