import eel
from abc import ABC, abstractmethod
from pymongo import MongoClient
from datetime import date

# === PENERAPAN ABSTRAKSI ===
# Kelas abstrak sebagai kontrak untuk koneksi database
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        """ Method untuk menghubungkan ke database """
        pass

# === PENERAPAN INHERITANCE ===
# Kelas konkrit yang mewarisi DatabaseConnection
class Database(DatabaseConnection):
    def __init__(self, host='mongodb://localhost:27017/', db_name='DB-Library'):
        """ Inisialisasi koneksi ke database MongoDB """
        self.host = host
        self.db_name = db_name
        self.client = None
        self.db = None
        self.connect()

    def connect(self):
        """ Membuat koneksi ke MongoDB """
        self.client = MongoClient(self.host)
        self.db = self.client[self.db_name]
        return self.db

# === PENERAPAN ENCAPSULATION ===
# Kelas dasar untuk entitas dengan method umum
class BaseEntity:
    def to_dict(self):
        """ Mengubah objek menjadi dictionary """
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

# Kelas User dengan atribut private (__)
class User(BaseEntity):
    def __init__(self, full_name, username, password, phone, email, role):
        """ Inisialisasi data User """
        self.__full_name = full_name
        self.__username = username  
        self.__password = password
        self.__phone = phone
        self.__email = email
        self.__role = role

    # === PENERAPAN PROPERTY ===
    # Getter untuk mengakses atribut private
    @property
    def full_name(self):
        return self.__full_name
        
    @property
    def username(self):
        return self.__username
        
    @property
    def role(self):
        return self.__role
    
    @property 
    def email(self):
        return self.__email
        
    @property
    def phone(self):
        return self.__phone

    # Setters with validation
    @full_name.setter
    def full_name(self, value):
        if value and len(value.strip()) > 0:
            self.__full_name = value.strip()
        else:
            raise ValueError("Full name cannot be empty")
            
    @email.setter
    def email(self, value):
        if value and '@' in value and '.' in value:
            self.__email = value.strip()
        else:
            raise ValueError("Invalid email format")
            
    @phone.setter
    def phone(self, value):
        if value and value.strip().isdigit() and len(value.strip()) >= 10:
            self.__phone = value.strip()
        else:
            raise ValueError("Phone number must be at least 10 digits")

    def to_dict(self):
        """ Mengubah User menjadi dictionary """
        return {
            'full_name': self.__full_name,
            'username': self.__username,
            'password': self.__password, 
            'phone': self.__phone,
            'email': self.__email,
            'role': self.__role
        }

# Kelas Book dengan atribut public
class Book(BaseEntity):
    def __init__(self, title, author, genre, stock, publish_year):
        """ Inisialisasi data Book """
        self.title = title
        self.author = author
        self.genre = genre
        self.stock = stock
        self.publish_year = publish_year

    def to_dict(self):
        """ Mengubah Book menjadi dictionary """
        return {
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'stock': self.stock,
            'publish_year': self.publish_year
        }

# === PENERAPAN REPOSITORY PATTERN ===
# Kelas abstrak untuk repository yang mengatur akses data
class BaseRepository(ABC):
    def __init__(self):
        self.db = Database().db  
    
    @abstractmethod
    def generate_id(self):
        """ Method untuk menghasilkan ID unik """
        pass

# Repository untuk User
class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.collection = self.db['users']  # Akses koleksi 'users' pada database

    def generate_id(self):
        """ Menghasilkan ID pengguna yang unik """
        return self.generate_user_id()

    def generate_user_id(self):
        """ Menghasilkan ID pengguna berdasarkan ID terakhir """
        last_user = self.collection.find_one({}, sort=[('user_id', -1)])
        if not last_user or 'user_id' not in last_user:
            return 'U001'
        last_num = int(last_user['user_id'][1:])
        new_num = last_num + 1
        return f'U{new_num:03d}'

    def add_user(self, user: User):
        """ Menambahkan pengguna baru ke database """
        user_dict = user.to_dict()
        user_dict['user_id'] = self.generate_id()  # Generate ID baru untuk pengguna
        return self.collection.insert_one(user_dict)

    def get_user(self, username):
        """ Mengambil data pengguna berdasarkan username """
        return self.collection.find_one({'username': username})

    def get_user_by_id(self, user_id):
        """ Mengambil data pengguna berdasarkan user_id """
        return self.collection.find_one({'user_id': user_id})

    def update_user(self, user_id, user_data):
        """ Memperbarui data pengguna """
        return self.collection.update_one(
            {'user_id': user_id},
            {'$set': user_data}
        )

# Repository untuk Book
class BookRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.collection = self.db['books']  # Akses koleksi 'books' pada database

    def generate_id(self):
        """ Menghasilkan ID buku yang unik """
        return self.generate_book_id()

    def generate_book_id(self):
        """ Menghasilkan ID buku berdasarkan ID terakhir """
        last_book = self.collection.find_one({}, sort=[('book_id', -1)])
        if not last_book or 'book_id' not in last_book:
            return 'B001'
        last_num = int(last_book['book_id'][1:])
        new_num = last_num + 1
        return f'B{new_num:03d}'

    def get_all_books(self):
        """ Mengambil semua buku yang ada di database """
        books = list(self.collection.find().sort("title", 1))
        for book in books:
            book['id'] = str(book['_id'])  
            book['book_id'] = book.get('book_id', 'B000')
            del book['_id']
        return books

    def get_book_by_id(self, book_id):
        """ Mengambil data buku berdasarkan book_id """
        book = self.collection.find_one({'book_id': book_id})
        if book:
            book['id'] = str(book['_id'])  
            del book['_id']
        return book

    def update_book(self, book_id, book_data):
        """ Memperbarui data buku """
        return self.collection.update_one(
            {'book_id': book_id},
            {'$set': book_data}
        )

    def delete_book(self, book_id):
        """ Menghapus buku berdasarkan book_id """
        return self.collection.delete_one({'book_id': book_id})

# Repository untuk Peminjaman
class BorrowRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.collection = self.db['borrows']  # Akses koleksi 'borrows' pada database

    def generate_id(self):
        """ Menghasilkan ID peminjaman yang unik """
        last_borrow = self.collection.find_one({}, sort=[('borrow_id', -1)])
        if not last_borrow or 'borrow_id' not in last_borrow:
            return 'BR001'
        last_num = int(last_borrow['borrow_id'][2:])
        new_num = last_num + 1
        return f'BR{new_num:03d}'

    def add_borrow(self, borrow_data):
        """ Menambahkan data peminjaman ke database """
        borrow_data['borrow_id'] = self.generate_id()
        return self.collection.insert_one(borrow_data)

    def get_user_borrows(self, user_id):
        """ Mengambil semua peminjaman oleh pengguna tertentu """
        return list(self.collection.find({'user_id': user_id}))

# === PENERAPAN SERVICE PATTERN ===
# Service untuk Authentication
class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()  # Inisialisasi repository pengguna

    def verify_password(self, stored_password, input_password):
        """ Verifikasi password pengguna """
        return stored_password == input_password

    def authenticate(self, username, password):
        """ Autentikasi pengguna berdasarkan username dan password """
        user = self.user_repo.get_user(username)
        if user and self.verify_password(user['password'], password):
            return {
                'success': True, 
                'role': user['role'],
                'user_id': user['user_id'],
                'username': user['username']
            }
        return {'success': False, 'message': 'Invalid username or password'}

# === INISIALISASI OBJEK ===
# Inisialisasi repository dan service
user_repo = UserRepository()
book_repo = BookRepository()
auth_service = AuthService()
borrow_repo = BorrowRepository()

# Fungsi untuk menginisialisasi admin jika belum ada
def initialize_admin():
    if not user_repo.get_user('admin'):
        admin = User(
            full_name='Administrator',
            username='admin',
            password='admin123',
            phone='081234567890',
            email='admin@library.com',
            role='admin'
        )
        user_repo.add_user(admin)

# === EXPOSED FUNCTIONS UNTUK EEL ===
# Fungsi-fungsi untuk dapat diakses dari JavaScript melalui Eel
@eel.expose
def login(login_data):
    """ Fungsi login untuk pengguna """
    return auth_service.authenticate(
        login_data['username'], 
        login_data['password']
    )

@eel.expose
def get_user_profile_data(user_id):
    """ Mengambil data profil pengguna berdasarkan user_id """
    try:
        user = user_repo.get_user_by_id(user_id)
        if user:
            del user['_id']  
            return {"success": True, "data": user}
        return {"success": False, "message": "User not found"}
    except Exception as e:
        return {"success": False, "message": str(e)}

@eel.expose
def update_user_profile_data(user_id, user_data):
    try:

        existing_user = user_repo.get_user_by_id(user_id)
        if not existing_user:
            return {"success": False, "message": "User not found"}
            
        user = User(
            full_name=existing_user['full_name'],
            username=existing_user['username'],
            password=existing_user['password'],
            phone=existing_user['phone'],
            email=existing_user['email'],
            role=existing_user['role']
        )
        
        if 'full_name' in user_data:
            user.full_name = user_data['full_name']
        if 'email' in user_data:
            user.email = user_data['email']
        if 'phone' in user_data:
            user.phone = user_data['phone']

        update_data = {
            'full_name': user.full_name,
            'email': user.email,
            'phone': user.phone
        }
        user_repo.update_user(user_id, update_data)
        return {"success": True, "message": "Profile updated successfully"}
        
    except ValueError as ve:
        return {"success": False, "message": str(ve)}
    except Exception as e:
        return {"success": False, "message": str(e)}


@eel.expose
def add_book(book_data):
    """ Menambahkan buku baru """
    try:
        new_book = Book(
            title=book_data['title'],
            author=book_data['author'],
            genre=book_data['genre'],
            stock=book_data['stock'],
            publish_year=book_data['publish_year']
        )
        book_dict = new_book.to_dict()
        book_dict['book_id'] = book_repo.generate_id()  # Generate book_id
        book_repo.collection.insert_one(book_dict)
        return {"success": True, "message": "Book added successfully"}
    except Exception as e:
        return {"success": False, "message": str(e)}

@eel.expose
def get_all_books():
    """ Mengambil semua buku dari koleksi """
    return book_repo.get_all_books()

@eel.expose
def get_book_details(book_id):
    """ Mengambil detail buku berdasarkan book_id """
    return book_repo.get_book_by_id(book_id)

@eel.expose
def update_book(book_id, book_data):
    """ Memperbarui data buku """
    return book_repo.update_book(book_id, book_data)

@eel.expose
def delete_book(book_id):
    """ Menghapus buku berdasarkan book_id """
    return book_repo.delete_book(book_id)

@eel.expose
def check_username_availability(username):
    """ Memeriksa ketersediaan username """
    try:
        existing_user = user_repo.get_user(username)
        return {
            "available": not existing_user,
            "message": "Username is available" if not existing_user else "Username already taken"
        }
    except Exception as e:
        return {"available": False, "message": str(e)}

@eel.expose
def register_user(user_data):
    """ Mendaftarkan pengguna baru """
    try:
        existing_user = user_repo.get_user(user_data['username'])
        if existing_user:
            return {"success": False, "message": "Username already taken. Please choose another username."}
            
        new_user = User(
            full_name=user_data['full_name'],
            username=user_data['username'],
            password=user_data['password'],
            phone=user_data['phone'],
            email=user_data['email'],
            role=user_data['role']
        )
        
        user_repo.add_user(new_user)
        return {"success": True, "message": "Registration successful"}
    except Exception as e:
        return {"success": False, "message": str(e)}

@eel.expose
def get_all_borrows():
    """ Mengambil semua data peminjaman """
    try:
        borrows = list(borrow_repo.collection.find())
        for borrow in borrows:
            # Menambahkan judul buku
            book = book_repo.get_book_by_id(borrow['book_id'])
            borrow['book_title'] = book['title'] if book else 'Unknown Book'
            
            # Menambahkan nama pengguna
            user = user_repo.get_user_by_id(borrow['user_id'])
            borrow['user_name'] = user['full_name'] if user else 'Unknown User'
            
            borrow['_id'] = str(borrow['_id'])
            
        return borrows
    except Exception as e:
        return []

@eel.expose
def borrow_book(book_id, user_id):
    """ Meminjam buku """
    try:
        book = book_repo.get_book_by_id(book_id)
        if not book or book['stock'] <= 0:
            return {"success": False, "message": "Book is not available"}

        # Mengurangi stok buku
        book_repo.update_book(book_id, {'stock': book['stock'] - 1})

        # Membuat data peminjaman
        borrow_data = {
            'user_id': user_id,
            'book_id': book_id,
            'borrow_date': date.today().strftime('%Y-%m-%d'),
            'return_date': None,
            'status': 'borrowed'
        }
        borrow_repo.add_borrow(borrow_data)

        return {"success": True, "message": "Book borrowed successfully"}
    except Exception as e:
        return {"success": False, "message": str(e)}

@eel.expose
def get_user_borrows(user_id):
    """ Mengambil semua peminjaman berdasarkan user_id """
    try:
        borrows = list(borrow_repo.collection.find({'user_id': user_id}))
        for borrow in borrows:
            book = book_repo.get_book_by_id(borrow['book_id'])
            borrow['book_title'] = book['title'] if book else 'Unknown Book'
            borrow['_id'] = str(borrow['_id'])
        return borrows
    except Exception as e:
        return []

@eel.expose
def return_book(borrow_id):
    """ Mengembalikan buku """
    try:
        borrow = borrow_repo.collection.find_one({'borrow_id': borrow_id})
        if not borrow:
            return {"success": False, "message": "Borrow record not found"}

        # Menambah stok buku kembali
        book = book_repo.get_book_by_id(borrow['book_id'])
        book_repo.update_book(borrow['book_id'], {'stock': book['stock'] + 1})

        # Memperbarui data peminjaman
        borrow_repo.collection.update_one(
            {'borrow_id': borrow_id},
            {
                '$set': {
                    'return_date': date.today().strftime('%Y-%m-%d'),
                    'status': 'returned'
                }
            }
        )

        return {"success": True, "message": "Book returned successfully"}
    except Exception as e:
        return {"success": False, "message": str(e)}
