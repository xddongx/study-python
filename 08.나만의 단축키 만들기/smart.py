from pynput.keyboard import Key, Listener, KeyCode
import win32api


# 단축키(어떤 키가 눌리면 호출이되는함수)
MY_HOT_KEYS = [
    # 어떤 키가 눌리면 호출이되는함수
    {'function1': {Key.ctrl_l, Key.alt_l, KeyCode(char='n')}},
    {'function2': {Key.ctrl_l, Key.shift}},
    {'function3': {Key.alt_l, Key.ctrl_l, KeyCode(char='g')}},

]

# 현재 어떤 키가 눌려져 잇는 키를 기억하는 집합(계속 눌려있기 때문데 중복 제거)
current_keys = set()

def function1():
    print('함수1 호출')
    win32api.WinExec('calc.exe')
def function2():
    print('함수2 호출')
    win32api.WinExec('notepad.exe')
def function3():
    print('함수3 호출')
    win32api.WinExec('c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

# key가 눌렸을 때
def key_pressed(key):
    print(f'Pressed {key}')
    for data in MY_HOT_KEYS:
        FUNCTION = list(data.keys())[0]         # function1
        KEYS = list(data.values())[0]           # 값

        if key in KEYS:                         # 현재 눌린 key가 KEYS에 있다면
            current_keys.add(key)               # 더해준다.

            if all(k in current_keys for k in KEYS):    # 모두 만죽을 한다면
                function = eval(FUNCTION)
                function()
            # checker = True
            # for k in KEYS:
            #     if key not in current_keys:     # KEYS에 없으니
            #         checker = False             # False
            #         break                       # 실행X
            #
            #     if checker:                     # True이면
            #         function = eval(FUNCTION)
            #         function()

#
def key_released(key):
    print(f'Released {key}')

    # key를 땟다면 제거
    if key in current_keys:
        current_keys.remove(key)

    # 동작이 끝낫다면
    if key == Key.esc:
        return False

# listener : 이벤트를 계속 감지하는..
with Listener(on_press=key_pressed, on_release=key_released) as listener:
    listener.join()
