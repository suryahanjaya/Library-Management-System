document.getElementById('registerForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        Swal.fire({
            title: 'Error!',
            text: 'Passwords do not match!',
            icon: 'error',
            confirmButtonText: 'OK'
        });
        return;
    }

    const userData = {
        full_name: document.getElementById('fullName').value,
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        password: password,
        role: 'user'
    };

    try {
        const result = await eel.register_user(userData)();
        
        if (result.success) {
            Swal.fire({
                title: 'Success!',
                text: 'Registration successful! Please login.',
                icon: 'success',
                confirmButtonText: 'OK'
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = 'login.html';
                }
            });
        } else {
            throw new Error(result.message);
        }
    } catch (error) {
        Swal.fire({
            title: 'Error!',
            text: error.message,
            icon: 'error',
            confirmButtonText: 'OK'
        });
    }
});

document.getElementById('username').addEventListener('input', async function() {
    const username = this.value;
    if (username.length > 0) {
        const result = await eel.check_username_availability(username)();
        
        if (!result.available) {
            this.classList.add('is-invalid');
            this.classList.remove('is-valid');
            this.setCustomValidity('Username already taken');
        } else {
            this.classList.add('is-valid');
            this.classList.remove('is-invalid');
            this.setCustomValidity('');
        }
    }
});

['password', 'confirmPassword'].forEach(id => {
    document.getElementById('toggle' + id.charAt(0).toUpperCase() + id.slice(1))
        .addEventListener('click', function() {
            const input = document.getElementById(id);
            const icon = this.querySelector('i');
            
            if (input.type === 'password') {
                input.type = 'text';
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                input.type = 'password';
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        });
});
