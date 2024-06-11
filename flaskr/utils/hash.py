import bcrypt

# Gera um hash de uma senha
def hash_password(password: str) -> str:
    # Gera um salt
    salt = bcrypt.gensalt()
    # Gera o hash da senha
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Verifica se uma senha corresponde ao hash
def check_password(password: str, hashed: str) -> bool:
    # Verifica se a senha corresponde ao hash
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

if __name__ == "__main__":
    # Exemplo de uso
    password = "minha_senha_secreta"
    hashed_password = hash_password(password)
    print("Senha original:", password)
    print("Senha hash:", hashed_password)

    # Verifica a senha
    is_correct = check_password(password, hashed_password)
    print("A senha está correta?", is_correct)
    