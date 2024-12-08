function logout() {
    // Clear user data from localStorage
    localStorage.clear();

    window.location.href = 'login.html';
}
