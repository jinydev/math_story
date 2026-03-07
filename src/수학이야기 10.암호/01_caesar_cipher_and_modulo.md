# 01. 숫자의 회전 윤회, 나머지 연산과 시저 암호

## 1. 학습 목표 (Learning Objectives)
* 암호학의 가장 기본 재료인 '나머지 연산(Modulo, mod)'의 주기성을 시계와 달력으로 이해합니다.
* 고대 로마의 율리우스 카이사르가 쓰던 '시저 암호(Caesar Cipher)'의 덧셈 매커니즘을 파이썬(Python) 파이프라인으로 구현해 봅니다.

## 2. 뱅글뱅글 도는 바퀴, 나머지 연산 (Modulo)
우리는 일상생활에서 이미 신기한 수학 연산을 매일 하고 있습니다.
"지금 오후 10시인데, **5시간 뒤**에 만나자!" 라고 하면, 우리는 $10 + 5 = 15$ 이므로 '15시(오후 3시)'라고 자연스럽게 계산합니다.
이 과정에서 10 더하기 5가 '15'지만 시계판은 12까지만 있으므로, 15를 $\mathbf{12}$로 나눈 **나머지인 3**을 구하게 됩니다.

> $15 \equiv 3 \pmod{12}$ (15와 3은 12로 나눈 나머지가 같으므로 수학적으로 한 몸이다)

이런 식으로 정해진 숫자의 쳇바퀴를 넘어가면 다시 처음(0)부터 사이클이 시작되는 연산을 수학에서는 **모듈러(Modulo) 연산**이라고 부르며 기호로 `%` 또는 `mod` 를 씁니다. 요일(7바퀴), 각도(360도 바퀴) 등은 모두 모듈러 연산의 산물입니다.

## 3. 영문 알파벳 26자의 모듈러 바퀴, 시저 암호
로마의 카이사르 장군은 부하들에게 기밀 편지를 보낼 때 단어를 이상하게 바꿔 보냈습니다. 알파벳을 전부 **3칸씩 뒤로 밀어서** 적은 것이죠. 
- $A \rightarrow D$, $B \rightarrow E$ ...

이것은 암호학사에서 최초로 등장한 치환 암호(Substitution Cipher)로 그 원리는 '나머지 연산' 그 자체입니다.
알파벳은 총 $\mathbf{26}$글자입니다. 수 체계로 바꾸면 $A=0, B=1, ... Y=24, Z=25$ 로 매핑됩니다.
만약 끝에 있는 $Z(25)$를 3칸 밀어버리면 범위를 훌쩍 벗어난 $28$이 되지만, 모듈러 26 규칙에 의해 $28 \pmod{26} = 2$, 즉 다시 $C$로 되돌아옵니다!

## 4. 파이썬 시저 암호 생성/해독기 (Python)
알파벳을 컴퓨터가 처리할 수 있는 아스키코드 번호(ASCII)로 바꾸고 쳇바퀴(%) 연산을 적용하는 파이썬 코드를 짜보겠습니다.

```python
def caesar_cipher_encrypt(text, shift_key):
    encrypted = ""
    for char in text.upper():
        # 영문 대문자인 경우에만 치환 수행
        if 'A' <= char <= 'Z':
            # 1. 아스키코드(ord) 활용, 'A'를 0으로 맞춤
            num = ord(char) - ord('A')
            
            # 2. 키(Key)만큼 밀어주고, 모듈러 26(%) 으로 쳇바퀴에 가둠
            shifted_num = (num + shift_key) % 26
            
            # 3. 0~25 숫자를 다시 문자로 복구
            encrypted += chr(shifted_num + ord('A'))
        else:
            encrypted += char # 띄어쓰기 등은 그대로 둠
    return encrypted

# 메시지 "MATH IS FUN" 을 3칸 밀어서 암호문으로 변환
original_text = "MATH IS FUN"
secret_key = 3
cipher_text = caesar_cipher_encrypt(original_text, secret_key)

print(f"■ 원본 메시지: {original_text}")
print(f"■ 시저 암호문 (Key={secret_key}): {cipher_text}")

# 해독(Decrypt)은 거꾸로 빼주면 됩니다 (-3 적용)
decrypted_text = caesar_cipher_encrypt(cipher_text, -secret_key)
print(f"■ 암호 해독문 (복구): {decrypted_text}")
```

#### 파이썬의 실행 결과 요약:
```text
■ 원본 메시지: MATH IS FUN
■ 시저 암호문 (Key=3): PDWK LV IXQ
■ 암호 해독문 (복구): MATH IS FUN
```
글자가 `PDWK LV IXQ` 로 이상하게 찌그러졌지만, 아군이 키 값인 '3번 뒤로 당겨(-3)'라는 사실만 알면 마법처럼 `MATH IS FUN` 원본으로 100% 복구됩니다.

## 5. 학습 정리 (Summary)
1. **나머지 연산 (Modulo)**: 나눗셈을 한 뒤 '나머지 값'만 취하는 수학의 강력한 바퀴 장치입니다. 시간이나 주기를 맞출 때 필수적입니다.
2. **시저 암호 (Caesar Cipher)**: 알파벳 26글자를 원판 바퀴에 나열해놓고 일정한 톱니 수(Key)만큼 $n$칸씩 회전시키는 치환 암호 방어막입니다.
