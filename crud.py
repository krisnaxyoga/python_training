import mysql.connector

# Koneksi ke database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # ganti kalau ada password
    database="tutorial_pyton_db"
)
cursor = db.cursor()

# CREATE
def create_user(name, email):
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = (name, email)
    cursor.execute(sql, val)
    db.commit()
    print("Data berhasil ditambahkan!")

# READ
def read_users():
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    for row in result:
        print(row)

# UPDATE
def update_user(id, name, email):
    sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    val = (name, email, id)
    cursor.execute(sql, val)
    db.commit()
    print("Data berhasil diupdate!")

# DELETE
def delete_user(id):
    sql = "DELETE FROM users WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    db.commit()
    print("Data berhasil dihapus!")

# Contoh penggunaan
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Tambah user")
        print("2. Lihat semua user")
        print("3. Ubah user")
        print("4. Hapus user")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            name = input("Nama: ")
            email = input("Email: ")
            create_user(name, email)
        elif pilihan == "2":
            read_users()
        elif pilihan == "3":
            id = input("ID user yang mau diubah: ")
            name = input("Nama baru: ")
            email = input("Email baru: ")
            update_user(id, name, email)
        elif pilihan == "4":
            id = input("ID user yang mau dihapus: ")
            delete_user(id)
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid.")
