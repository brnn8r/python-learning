def recursive_reverse_string(s: str):
    def tail_helper(inner_s: str, accumulated: str):
        if len(inner_s) <= 0:
            return accumulated
        return tail_helper(inner_s[:-1], accumulated + inner_s[-1:])

    return tail_helper(s, "")


def reverse_string(s: str):
    return s[::-1]


if __name__ == "__main__":
    me = "steve"
    print(f"Hello {reverse_string(me)}")





