#문자열 응용하기

#1. 문자열 접근
'''
a='Hello, world!'
print(a[0])
print(a[4])
print(a[6])

print(len(a))
'''
#2. 문자열에 다른 문자 할당

#a[0]='T' #문자열 내용은 할당으로 변경할 수 없음 (튜플처럼)

#3. 인덱스 범위로 접근
'''
print(a[4:7])
print(a[:5])
print(a[5:])
print(a[:])
print(a[-1])
'''
#4. 문자열에서 for 문과 in 연산자 사용
'''
for i in 'Hello':
    print(i, end=' ')
print()

print('e' in 'Hello')
print('w' in 'Hello')
'''
#5. 문자열 메서드 사용
'''
#1) .replace 문자열 내의 문자를 바꾼다.

s='Hello, world'
print(s.replace('world','Python'))
print(s)

#2) .split 공백을 기준으로 문자열을 분리하여 리스트 생성

s='apple pear grape pineapple orange'
print(s.split())
print(s)

s='apple,pear,grape,pineapple,orange'
print(s.split(','))
print(s)
c=s.split(',')

#3) .join 구분자 문자열과 리스트의 문자열 요소를 연결함

a='+'
print(a.join(c))
b='-'
print(b.join(c))

#4) .upper .lower 문자열 모두를 대문자 또는 소문자로 만든다.

d='apple'
print(d.upper())
e=d.upper()
print(e.lower())

#5) .lstrip .rstrip .strip 문자열의 공백을 제거

s='   python   '
print(s.lstrip())
print(s.rstrip())
print(s.strip())

#6) .zfill 지정된 길이에 맞춰서 문자열의 왼쪽에 '0'을 채움

print('35'.zfill(4))
print('3.5'.zfill(4))

#7) .index 문자열을 찾아 인덱스를 반환 (없으면 에러)

s='apple pineapple'
print(s.index('pl'))
#print(s.index('t')) #에러

#8) .find .rfind 왼쪽부터 찾아 인덱스 반환, 오른쪽부터 찾아 인덱스 반환 (없으면 -1 반환)

print(s.find('pl'))
print(s.rfind('pl'))
print(s.find('b'))

#9) .count 문자열이 몇 번 나오는지 세는 메서드

print(s.count('p'))
'''
#6. 회문 판별
'''
word=input('회문 판별 단어는?')
#print(word)
word_replace=word.replace(" ","")
#print(word_replace)
is_palindrome=True #판별 여부 저장변수
for i in range(len(word_replace)//2):
    if word_replace[i] != word_replace[-1-i]:
        is_palindrome=False
        break
print(is_palindrome)
'''
#7. N-gram 만들기
'''
text='Hello'
#2-gram
for i in range(len(text)-1):
    print(text[i],text[i+1],sep="")
#3-gram
for i in range (len(text)-2):
    print(text[i],text[i+1],text[i+2],sep="")
#N-gram
'''
#8. 문자열 크기 비교
#목록 문자열 또는 정렬이 가능한 경우 순서에 따른 크기비교가 가능하다.
print('A'<='C')
print('g'>'h')
print('c'>='A')
print('A'<='c'<='E') #양쪽 구간일 때는 대소문자 구분
print('A'<='C'<='E')
