document.addEventListener('DOMContentLoaded', loadBorrowedBooks);

async function loadBorrowedBooks() {
    const userId = localStorage.getItem('user_id');
    if (!userId) {
        window.location.href = 'login.html';
        return;
    }

    try {
        const borrowedBooks = await eel.get_user_borrows(userId)();
        const borrowedBooksList = document.getElementById('borrowedBooksList');
        
        if (!borrowedBooks || borrowedBooks.length === 0) {
            borrowedBooksList.innerHTML = '<tr><td colspan="5">No borrowed books found</td></tr>';
            return;
        }

        borrowedBooksList.innerHTML = '';
        borrowedBooks.forEach(borrow => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${borrow.book_title}</td>
                <td>${borrow.borrow_date}</td>
                <td>${borrow.return_date || '-'}</td>
                <td>${borrow.status}</td>
                <td>
                    ${borrow.status === 'borrowed' ? 
                    `<button class="btn btn-success btn-sm" onclick="returnBook('${borrow.borrow_id}')">Return Book</button>` : 
                    '-'}
                </td>
            `;
            borrowedBooksList.appendChild(row);
        });
    } catch (error) {
        console.error('Error loading borrowed books:', error);
        document.getElementById('borrowedBooksList').innerHTML = 
            '<tr><td colspan="5">Error loading borrowed books</td></tr>';
    }
}

async function returnBook(borrowId) {
    try {
        const result = await eel.return_book(borrowId)();
        if (result.success) {
            Swal.fire({
                title: 'Success!',
                text: result.message,
                icon: 'success'
            }).then(() => {
                loadBorrowedBooks();
            });
        } else {
            Swal.fire('Error', result.message, 'error');
        }
    } catch (error) {
        Swal.fire('Error', 'Failed to return book', 'error');
    }
}
