

def BeforeAfter(month,day):
    m=2
    d=18
    if month<m or month==m and day<d:
        print('Before')
    elif month>m or month==m and day>d:
        print('After')
    elif month==m and day==d:
        print('Special')





month=int(input())
day=int(input())
BeforeAfter(month,day)
