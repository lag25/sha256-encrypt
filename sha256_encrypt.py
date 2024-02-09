import argparse
import hashlib

def sha256_encrypt(data):
    """Encrypts the input data using SHA-256."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

def main():
    parser = argparse.ArgumentParser(description='Encrypt data using SHA-256.')
    parser.add_argument('data', help='Input data to be encrypted')

    args = parser.parse_args()

    input_data = args.data
    encrypted_data = sha256_encrypt(input_data)

    print(f'Input Data: {input_data}')
    print(f'Encrypted Data (SHA-256): {encrypted_data}')

if __name__ == '__main__':
    main()
