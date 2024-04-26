class AuthLocs:
    login_button = ('xpath', '//*[@id="login-button"]')
    user_field = ('xpath', '//*[@data-test="username"]')
    password_field = ('xpath', '//*[@data-test="password"]')
    error_message = ('xpath', '//*[@data-test="error"]')

class AuthData:
    valid_username1 = 'standard_user'
    valid_username2 = 'locked_out_user'
    valid_username3 = 'problem_user'
    valid_username4 = 'performance_glitch_user'
    valid_password = 'secret_sauce'
    invalid_username = 'A'
    invalid_password = '.'
    login_button_name = 'LOGIN'
    auth_locked_message = 'Epic sadface: Sorry, this user has been locked out.'
    auth_error_message1 = 'Epic sadface: Username is required'
    auth_error_message2 = 'Epic sadface: Password is required'
    auth_error_message3 = 'Epic sadface: Username and password do not match any user in this service'