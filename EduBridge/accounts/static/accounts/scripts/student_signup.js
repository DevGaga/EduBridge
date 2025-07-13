// Example: confirm password check (if form includes password confirmation)
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const password = document.querySelector('input[name="password1"]');
    const confirm = document.querySelector('input[name="password2"]');

    if (password && confirm) {
        form.addEventListener('submit', function (e) {
            if (password.value !== confirm.value) {
                e.preventDefault();
                alert('Passwords do not match!');
            }
        });
    }
});
