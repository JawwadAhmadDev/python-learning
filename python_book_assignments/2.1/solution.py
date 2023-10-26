message: str = "This is my first program in python"

# Methods to combine string and variables
# 1st method - using double quotes
print("Message: " + message)

# 2nd method - using single quotes
print('Message: ' + message)

# 3rd method - using triple double quotes
print("""Message: """ + message)

# 4th method - using triple single quotes
print('''Message: ''' + message)

# 5th method - using f-string
print(f"Message: {message}")

# 6th method - using f-string with tripple quotes
print(f'''Message: {message}''')

# 7th method - using % method as previously used in c language
print(f'Message: %s' %(message))

# 8th method - using format method
print('''Message: {}'''.format(message))