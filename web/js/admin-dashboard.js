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
                    <button class="btn btn-warning btn-sm" onclick="editBook('${book.book_id}')">Edit</button>
                    <button class="btn btn-danger btn-sm" onclick="deleteBook('${book.book_id}')">Delete</button>
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

async function editBook(bookId) {
    const book = await eel.get_book_details(bookId)();
    if (book) {
        Swal.fire({
            title: 'Edit Book',
            html: `
                <input id="title" class="swal2-input" placeholder="Title" value="${book.title}">
                <input id="author" class="swal2-input" placeholder="Author" value="${book.author}">
                <input id="genre" class="swal2-input" placeholder="Genre" value="${book.genre}">
                <input id="stock" class="swal2-input" type="number" placeholder="Stock" value="${book.stock}">
                <input id="publish_year" class="swal2-input" type="number" placeholder="Publish Year" value="${book.publish_year}">
            `,
            showCancelButton: true,
            confirmButtonText: 'Save',
            preConfirm: () => {
                return {
                    title: document.getElementById('title').value,
                    author: document.getElementById('author').value,
                    genre: document.getElementById('genre').value,
                    stock: parseInt(document.getElementById('stock').value),
                    publish_year: parseInt(document.getElementById('publish_year').value)
                }
            }
        }).then(async (result) => {
            if (result.isConfirmed) {
                await eel.update_book(bookId, result.value)();
                loadBooks();
                Swal.fire('Saved!', 'Book has been updated.', 'success');
            }
        });
    }
}

async function deleteBook(bookId) {
    const result = await Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Yes, delete it!'
    });

    if (result.isConfirmed) {
        await eel.delete_book(bookId)();
        loadBooks();
        Swal.fire('Deleted!', 'Book has been deleted.', 'success');
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
