import string


def is_valid_IPv4(string):
    ipv4 = string.split(".")
    if len(ipv4) == 4:
        for part in ipv4:
            if part.isdecimal() and int(part) < 256:
                is_IPv4 = True
            else:
                is_IPv4 = False
                break
    else:
        is_IPv4 = False
    return is_IPv4


def is_valid_IPv6(string_line):
    ipv6 = string_line.split(":")
    if len(ipv6) == 8:
        for part in ipv6:
            for letter in part:
                if letter in string.hexdigits:
                    is_IPv6 = True
                else:
                    is_IPv6 = False
                    break
    else:
        is_IPv6 = False
    return is_IPv6


def main(input_string):
    for line in input_string.split("\n"):
        print(line)
        if not line == input_string.split("\n")[0]:
            if is_valid_IPv4(line):
                print("IPv4")
            elif is_valid_IPv6(line):
                print("IPv6")
            else:
                print("Neither")


if __name__ == "__main__":
    main(input())
