document.getElementById('addBookForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const bookData = {
        title: document.getElementById('bookTitle').value,
        author: document.getElementById('bookAuthor').value,
        genre: document.getElementById('bookGenre').value,
        stock: parseInt(document.getElementById('bookStock').value),
        publish_year: parseInt(document.getElementById('bookPublishYear').value)
    };

    try {
        const result = await eel.add_book(bookData)();
        
        if (result.success) {
            Swal.fire({
                title: 'Success!',
                text: result.message,
                icon: 'success',
                confirmButtonText: 'OK'
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = 'admin-dashboard.html';
                }
            });
        } else {
            throw new Error(result.message);
        }

    } catch (error) {
        Swal.fire({
            title: 'Error!',
            text: 'Failed to add book: ' + error.message,
            icon: 'error',
            confirmButtonText: 'OK'
        });
    }
});
