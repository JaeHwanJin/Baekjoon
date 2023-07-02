def solution(s):    
    s = list(map(str, s))
    st = []
    for i in s:
        if len(st) == 0:
            st.append(i)
        else:
            if st[-1] == i:
                st.pop()
            else:
                st.append(i)
    if len(st) == 0:
        answer = 1
    else:
        answer = 0
    return answer