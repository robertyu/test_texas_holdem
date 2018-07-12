def get_num(m):
    if m == 'A':
        return 14
    elif m == 'K':
        return 13
    elif m == 'Q':
        return 12
    elif m == 'J':
        return 11
    elif m == 'T':
        return 10
    else:
        return int(m)


def group_consecutives(vals, step=1):
    """Return list of consecutive lists of numbers from vals (number list)."""
    run = []
    result = [run]
    expect = None
    for v in vals:
        if (v == expect) or (expect is None):
            run.append(v)
        else:
            run = [v]
            result.append(run)
        expect = v + step
    return result


def after_flop_run(n0, n1, c0, c1, bc, players_num, bb_rate):
    flags = {'allin': False, 'bet': False}
    from collections import Counter
    hand = [(get_num(b[0]), b[1]) for b in bc]
    hand.extend([(n0, c0), (n1, c1)])

    # test s
    hand = [(11, 'C'), (12, 'H'), (6, 'S'), (7, 'S'), (2, 'S')]
    # test p
    cs = Counter([h[1] for h in hand])
    ns = [h[0] for h in hand]
    ns.sort()
    ns = group_consecutives(ns)
    ns_c = Counter([h[0] for h in hand])

    # check straight/pair first then flush
    if cs[0] == 5:
        # flush

        # Straight
        if 5 in [len(k) for k in ns]:
            flags['allin'] = True
        elif 4 in [len(k) for k in ns]:
            flags['allin'] = True
        else:
            if bb_rate > 0.15:
                flags['allin'] = True

        # pair

    elif cs[0] == 4:
        if len(hand) == 7:
            # river
            ns_c.pop(0, None)
            pass

    if c0 == c1:
        # suit -> flush, out 11, 50 - (p * 2) 取 2, 中 11
        max_count = 0
        counter_result = Counter(hand)
        # hand -> flush
        # hand -> flush straight
        # hand -> two pair
        # hand -> 3k
        for c in counter_result:
            if max_count == 0:
                max_count = counter_result[c]
        if max_count == 4:
            flags['allin'] = True
    else:
        if n0 == n1:
            # pair -> 3k, out
            # pair -> fh
            # pair -> 4k
            pass
        else:
            if abs(n0 - n1) < 5:
                if c0 == c1:
                    # high card - > flush straight
                    pass
                else:
                    # high card - > Straight
                    pass

    return flags


# hand = [(11, 'C'), (12, 'H'), (6, 'S'), (7, 'S'), (2, 'S')]
print(after_flop_run(11, 12, 'C', 'H', ['6S', '7S', '2S'], 15, 0.12))
