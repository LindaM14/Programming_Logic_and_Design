# take code from python tutor and make it uppercase
# .upper() makes strings go uppercase
def greeting(name):
    message = f'Hello {name}!!!'.upper()
    return message

# !!! after name will print in (hello_message) string

def main():
    username = 'Miriam'
    hello_message = greeting(username)
    print(hello_message)

main()
