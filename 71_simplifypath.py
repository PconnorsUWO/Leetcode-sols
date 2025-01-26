# starts with /
# aa single period represents the cur dir
# a double preiod represents the prev dir
# multiple consecutive slashes are treatred as a single /
# ......... are valid dir names


def simplifyPath(path: str) -> str:
    path = path.split("/")
    res = ""
    for i in path:
        if i == "":
            continue
        elif i == "..":
            while res and res[-1] != "/":
                res = res[:-1]
            res = res[:-1]
            continue
        elif i == '.':
            continue
        text = "/" + i
        res += text
    if res == "":
        return "/"
    return res

case1 = "/home/"
case2 = "/home/user/Documents/../Pictures"
case3 = "/home/user/../../"

print(simplifyPath(case1))
print(simplifyPath(case2))
print(simplifyPath(case3))
