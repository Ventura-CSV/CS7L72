import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = '10\n25\n15\n35\n50'
    # sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    rdlst = list(map(int, lines[0].split()))
    print(rdlst)
    mval = min(rdlst)
    midx = rdlst.index(mval)

    regex_string = r'[\w,\W]*' + str(mval)
    regex_string += r'[\w,\W]*' + str(midx)
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[1])
    assert res != None
    print(res.group())
