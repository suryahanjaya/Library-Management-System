document.addEventListener('DOMContentLoaded', loadAllBorrows);

async function loadAllBorrows() {
    try {
        const borrows = await eel.get_all_borrows()();
        const borrowList = document.getElementById('borrowList');
        
        if (!borrows || borrows.length === 0) {
            borrowList.innerHTML = '<tr><td colspan="4">No borrowing records found</td></tr>';
            return;
        }

        borrowList.innerHTML = '';
        borrows.forEach(borrow => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${borrow.book_title}</td>
                <td>${borrow.user_name}</td>
                <td>${borrow.borrow_date}</td>
                <td>${borrow.status}</td>
            `;
            borrowList.appendChild(row);
        });
    } catch (error) {
        console.error('Error loading borrows:', error);
        document.getElementById('borrowList').innerHTML = 
            '<tr><td colspan="4">Error loading borrowing data</td></tr>';
    }
}
