def main():
    data = {'website': 'google'}
    try:
        d = data['url']
        print(d)
    except:
        print('print Except')
        return 'return Except'
    finally:
        print('print Finally')


d = 10
asd = main()
print(asd)
