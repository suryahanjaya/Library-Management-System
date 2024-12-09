document.addEventListener("contextmenu", (e) => e.preventDefault());
document.onkeydown = (e) => {
    if (e.key == 123) {
        e.preventDefault(); 
    }
    if (e.ctrlKey && e.shiftKey && e.key == 'I') {
        e.preventDefault(); 
    }
    if (e.ctrlKey && e.shiftKey && e.key == 'C') {
        e.preventDefault();
    }
    if (e.ctrlKey && e.shiftKey && e.key == 'J') {
        e.preventDefault(); 
    }
    if (e.ctrlKey && e.key == 'U') {
        e.preventDefault(); 
    }
};

function logout() {

    localStorage.clear();

    window.location.href = 'login.html';
}
