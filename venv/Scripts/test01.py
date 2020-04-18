import re

def main():
    content = '0928012729'
    result = re.match(r'(?:0|886-?)9\d{2}-?\d{6}', content)
    if result:
        print("123")

if __name__ == '__main__':
    main()