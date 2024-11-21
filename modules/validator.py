from password_validator import PasswordValidator

def validate_password(password):    
    validator = PasswordValidator()
    
    validator \
        .min(8) \
        .has().digits() \
        .has().lowercase() \
        .has().uppercase() \
        .has().symbols()

    is_valid = validator.validate(password)
    
    if is_valid:
        password_score = 4
    else:
        password_score = sum([
            validator.has().digits().validate(password),
            validator.has().lowercase().validate(password),
            validator.has().uppercase().validate(password),
            validator.has().symbols().validate(password),
            validator.min(8).validate(password)
        ])
    
    if password_score <= 2:
        return "Weak Password"
    elif 3 <= password_score < 4:
        return "Moderate Password"
    elif password_score == 4:
        return "Strong Password"