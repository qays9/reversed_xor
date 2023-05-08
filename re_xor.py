with open("twoside.jpg", "rb") as file:
    OF = 4 #number of the every hex   
    sig = b""
    sig_read  = bytearray(file.read(OF))

    # Reversing         echo "aHR0cHM6Ly9naXRodWIuY29tL3FheXM5L3JldmVyc2VkX3hvci9ibG9iL21haW4vdHdvc2lkZV9yZS56aXAK"
    while sig_read:
        sig += sig_read[::-1]
        sig_read = file.read(OF)       

# XOR the binary data with key 0xff
sig_encrypted = bytes([b ^ 0xff for b in sig])

# Write the encrypted data to a new file
with open('twoside_re.jpg', 'wb') as f:
    f.write(sig_encrypted)
