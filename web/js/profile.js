document.addEventListener('DOMContentLoaded', async function() {
    const userId = localStorage.getItem('user_id');
    if (!userId) {
        window.location.href = 'login.html';
        return;
    }

    // Load user profile
    const result = await eel.get_user_profile_data(userId)();
    if (result.success) {
        const user = result.data;
        document.getElementById('userId').value = user.user_id;
        document.getElementById('fullName').value = user.full_name;
        document.getElementById('username').value = user.username;
        document.getElementById('email').value = user.email;
        document.getElementById('phone').value = user.phone;
        document.getElementById('role').value = user.role;
    }
});

document.getElementById('profileForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const userData = {
        full_name: document.getElementById('fullName').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value
    };

    const userId = document.getElementById('userId').value;
    const result = await eel.update_user_profile_data(userId, userData)();

    if (result.success) {
        Swal.fire({
            title: 'Success!',
            text: result.message,
            icon: 'success',
            confirmButtonText: 'OK'
        });
    } else {
        Swal.fire({
            title: 'Error!',
            text: result.message,
            icon: 'error',
            confirmButtonText: 'OK'
        });
    }
});
