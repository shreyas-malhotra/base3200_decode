import base64

input_file = 'base3200_encoded_input_file'

for _ in range(50):
    with open(input_file, 'r') as f:
        encoded_data = f.read().strip()

    decoded_data = base64.b64decode(encoded_data).decode('utf-8')

    with open(input_file, 'w') as f:
        f.write(decoded_data)
