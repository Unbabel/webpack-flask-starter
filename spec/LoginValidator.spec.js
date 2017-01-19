/* global describe it expect */
import LoginValidator from '../src/js/LoginValidator';

describe('LoginValidator', () => {
  it('username must have minimum of 5 characters and only numbers and letters', () => {
    expect(LoginValidator.usernameIsValid('')).toEqual(false);
    expect(LoginValidator.usernameIsValid('a')).toEqual(false);
    expect(LoginValidator.usernameIsValid('abcs ')).toEqual(false);
    expect(LoginValidator.usernameIsValid('ab ')).toEqual(false);
    expect(LoginValidator.usernameIsValid('abcde')).toEqual(true);
  });
  it('password must have between of 8 and 20 characters and only numbers and letters', () => {
    expect(LoginValidator.passwordIsValid('')).toEqual(false);
    expect(LoginValidator.passwordIsValid('a')).toEqual(false);
    expect(LoginValidator.passwordIsValid('abcs ')).toEqual(false);
    expect(LoginValidator.passwordIsValid('ab ')).toEqual(false);
    expect(LoginValidator.passwordIsValid('abcqqq de')).toEqual(false);
    expect(LoginValidator.passwordIsValid('abcde55')).toEqual(false);
    expect(LoginValidator.passwordIsValid('abcde5aadd5')).toEqual(true);
  });
});
