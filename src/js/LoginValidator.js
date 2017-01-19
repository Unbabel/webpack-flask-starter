const LoginValidator = {
  usernameIsValid(username) {
    const match = username.match(/^[\w\d]{5,}$/);
    return match !== null && match.length > 0;
  },
  passwordIsValid(password) {
    const match = password.match(/^[\w\d]{8,20}$/);
    return match !== null && match.length > 0;
  },
};

export default LoginValidator;
