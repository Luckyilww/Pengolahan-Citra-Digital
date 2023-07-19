from PIL import Image

def hide_message(image_path, message):
    # Buka gambar
    image = Image.open(image_path)
    # Konversi gambar ke mode RGB
    image = image.convert("RGB")
    # Ubah pesan menjadi bit
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    message_length = len(binary_message)
    
    width, height = image.size
    max_message_length = width * height * 3
    
    # Periksa apakah pesan dapat disisipkan dalam citra
    if message_length > max_message_length:
        print("Pesan terlalu panjang. Gunakan gambar dengan ukuran yang lebih besar.")
        return
    
    data_index = 0
    for y in range(height):
        for x in range(width):
            # Dapatkan piksel RGB pada posisi (x, y)
            r, g, b = image.getpixel((x, y))
            
            # Ubah nilai piksel menjadi biner
            r = format(r, '08b')
            g = format(g, '08b')
            b = format(b, '08b')
            
            # Sisipkan bit pesan dalam bit terakhir piksel
            if data_index < message_length:
                r = r[:-1] + binary_message[data_index]
                data_index += 1
            if data_index < message_length:
                g = g[:-1] + binary_message[data_index]
                data_index += 1
            if data_index < message_length:
                b = b[:-1] + binary_message[data_index]
                data_index += 1
            
            # Ubah kembali nilai piksel menjadi integer
            r = int(r, 2)
            g = int(g, 2)
            b = int(b, 2)
            
            # Set piksel dengan nilai baru
            image.putpixel((x, y), (r, g, b))
    
    # Simpan gambar dengan pesan tersembunyi
    image.save("image_with_message.png")
    print("Pesan berhasil disisipkan dalam citra.")
    

def extract_message(image_path):
    # Buka gambar dengan pesan tersembunyi
    image = Image.open(image_path)
    # Konversi gambar ke mode RGB
    image = image.convert("RGB")
    
    binary_message = ""
    
    width, height = image.size
    for y in range(height):
        for x in range(width):
            # Dapatkan piksel RGB pada posisi (x, y)
            r, g, b = image.getpixel((x, y))
            
            # Ubah nilai piksel menjadi biner
            r = format(r, '08b')
            g = format(g, '08b')
            b = format(b, '08b')
            
            # Dapatkan bit terakhir piksel
            binary_message += r[-1]
            binary_message += g[-1]
            binary_message += b[-1]
    
    # Konversi bit pesan menjadi karakter
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
    
    return message


# Contoh penggunaan
image_path = "images.png"
message = "Ini adalah pesan rahasia!"

hide_message(image_path, message)

extracted_message = extract_message("image_with_message.png")
print("Pesan yang diekstraksi:", extracted_message)
