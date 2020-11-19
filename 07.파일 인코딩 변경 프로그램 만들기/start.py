import os, argparse
from chardet import detect

# 폴더 안에 있는 파일 찾기
def search_dir(dirname):
    result_list = []                    # 찾은 파일의 path를 저장할 리스트
    file_names = os.listdir(dirname)    # 경로안에 파일 이름 리스트['bbb.txt', 'folder1', 'start.py']

    for filename in file_names:
        full_path = os.path.join(dirname, filename)         # 폴더, 파일 path

        if os.path.isdir(full_path):                        # 폴더를 찾으면 다시 들어가 파일을 찾는다.
            result_list.extend(search_dir(full_path))
        else:
            result_list.append(full_path)                   # 파일의 경로를 리스트에 담는다.
    return result_list

def get_encoding_type(filepath):
    with open(filepath, 'rb') as f:         # 바이너리
        rawdata = f.read()                  # 바이너리 데이터

    codec = detect(rawdata)                 # 파일의 encoding, confidence, language 등....
    return codec['encoding']                # encoding만 가져온다.

INCLUDE_EXT_LIST = ['.txt', '.smi']

# parse = argparse.ArgumentParser()
# parse.add_argument('-f', type=str)
# parse.add_argument('-e', nargs='+')
# args = parse.parse_args()
#
# if args.f is not None:
#     path = args.f
#     filelists = search_dir(path)
#
#     if args.e is not None:
#         if len(args.e) > 0:
#             # INCLUDE_EXT_LIST = []
#             # for e in args.e:
#             #     if e[0:1] == '.':
#             #         INCLUDE_EXT_LIST.append(e)
#             #     else:
#             #         INCLUDE_EXT_LIST.append('.'+e)
#
#             INCLUDE_EXT_LIST = [e.lower() if e[0:1] == '.' else '.{}'.format(e.lower()) for e in args.e]
#             print(INCLUDE_EXT_LIST)
path = 'c:\\workspace\\study-python\\07.파일 인코딩 변경 프로그램 만들기'
filelists = search_dir(path)

# c:\\...\..\aaa.txt
for file in filelists:
    filename, ext = os.path.splitext(file)      # 파일의 이름, 확장자 분리

    tempfile = filename + '_tmp' + ext          # 잠깐 저장될 파일이름
    if ext.lower() in INCLUDE_EXT_LIST:         # 확장자 중 ext 리스트에 있고
        encoding = get_encoding_type(file)
        if encoding.lower().find('utf') < 0:    # utf가 아닌 확장자
            try:
                with open(file, 'r') as read, open(tempfile, 'w', encoding='utf-8') as write:       # 파일을 읽는다 read라고 하고, 잠깐 저장해둔 파일을 쓴다 write로 encoding은 utf-8
                    write.write(read.read())            # write를 쓴다, read를 읽어서...

                os.unlink(file)                         # 원본 파일은 지운다.
                os.rename(tempfile, file)               # 잠깐 저장해둔걸 원본 파일 이름으로 바꾼다.
                print(f'{file}이 저장되었습니다.')
            except:
                pass
            finally:
                if os.path.exists(tempfile):        # 잠깐 저장해둔 파일이 있다면
                    os.unlink(tempfile)             # 잠깐 저장해둔 파일 지운다.


