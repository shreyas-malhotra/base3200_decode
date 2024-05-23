import base64

print("Make sure that this script is being execute in the same directory, that the input file is stored in.")

file_name = input("Please enter the name of the input file: ")

for _ in range(50):
    with open(file_name, 'r') as f:
        encoded_data = f.read().strip()

    decoded_data = base64.b64decode(encoded_data).decode('utf-8')

    with open(file_name, 'w') as f:
        f.write(decoded_data)

print("The input file should now have be overwritten with the decoded data.")
