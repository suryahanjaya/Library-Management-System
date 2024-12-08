document.addEventListener('DOMContentLoaded', loadBooks);

async function loadBooks() {
    try {
        const books = await eel.get_all_books()();
        console.log('Books received:', books);
        
        if (!books || books.length === 0) {
            document.getElementById('bookList').innerHTML = '<tr><td colspan="6">No books found</td></tr>';
            return;
        }

        const bookList = document.getElementById('bookList');
        bookList.innerHTML = '';

        books.forEach(book => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${book.title || 'N/A'}</td>
                <td>${book.author || 'N/A'}</td>
                <td>${book.genre || 'N/A'}</td>
                <td>${book.publish_year || 'N/A'}</td>
                <td>${book.stock > 0 ? 'Available' : 'Out of Stock'}</td>
                <td>
                    <button class="btn btn-info btn-sm" onclick="viewDetails('${book.book_id}')">Details</button>
                    <button class="btn btn-warning btn-sm" onclick="borrowBook('${book.book_id}')">Borrow</button>
                </td>
            `;
            bookList.appendChild(row);
        });
    } catch (error) {
        console.error('Error loading books:', error);
        document.getElementById('bookList').innerHTML = '<tr><td colspan="6">Error loading books</td></tr>';
    }
}

async function viewDetails(bookId) {
    const book = await eel.get_book_details(bookId)();
    if (book) {
        Swal.fire({
            title: 'Book Details',
            html: `
                <div class="text-left">
                    <p><strong>Book ID:</strong> ${book.book_id}</p>
                    <p><strong>Title:</strong> ${book.title}</p>
                    <p><strong>Author:</strong> ${book.author}</p>
                    <p><strong>Genre:</strong> ${book.genre}</p>
                    <p><strong>Published:</strong> ${book.publish_year}</p>
                    <p><strong>Stock:</strong> ${book.stock}</p>
                </div>
            `,
            icon: 'info'
        });
    }
}

async function borrowBook(bookId) {
    const userId = localStorage.getItem('user_id');
    if (!userId) {
        Swal.fire('Error', 'Please login first', 'error');
        return;
    }

    const book = await eel.get_book_details(bookId)();
    
    const result = await Swal.fire({
        title: 'Confirm Borrowing',
        html: `
            <div class="text-left">
                <p><strong>Title:</strong> ${book.title}</p>
                <p><strong>Author:</strong> ${book.author}</p>
                <p><strong>Genre:</strong> ${book.genre}</p>
                <p><strong>Published:</strong> ${book.publish_year}</p>
                <p><strong>Stock Available:</strong> ${book.stock}</p>
            </div>
            <p class="mt-3">Are you sure you want to borrow this book?</p>
        `,
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: 'Yes, Borrow',
        cancelButtonText: 'Cancel'
    });

    if (result.isConfirmed) {
        const borrowResult = await eel.borrow_book(bookId, userId)();
        
        if (borrowResult.success) {
            Swal.fire({
                title: 'Success!',
                text: borrowResult.message,
                icon: 'success'
            }).then(() => {
                loadBooks();
            });
        } else {
            Swal.fire('Error', borrowResult.message, 'error');
        }
    }
}

document.getElementById('searchBooks').addEventListener('input', function(e) {
    const searchText = e.target.value.toLowerCase();
    const rows = document.querySelectorAll('#bookList tr');
    
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(searchText) ? '' : 'none';
    });
});
