from pynput.keyboard import Key, Listener, KeyCode

# key가 눌렸을 때
def key_pressed(key):
    print(f'Pressed {key}')

#
def key_released(key):
    print(f'Released {key}')

    # 동작이 끝낫다면
    if key == Key.esc:
        return False

# listener : 이벤트를 계속 감지하는..
with Listener(on_press=key_pressed, on_release=key_released) as listener:
    listener.join()
