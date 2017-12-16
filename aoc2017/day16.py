#!/usr/bin/env python3
# -*- coding: utf-8 -*-


ops = []
with open('input/day16') as f:
    inpt = f.read().strip().split(',')
    for e in inpt:
        ops.append({
            's': lambda e: (e[0], int(e[1:])),
            'x': lambda e: (e[0], tuple(int(n) for n in e[1:].split('/'))),
            'p': lambda e: (e[0], tuple(v for v in e[1:].split('/')))
        }[e[0]](e))


class Operator():
    progs = 'abcdefghijklmnop'

    def __init__(self, ops):
        self.fcnt = {'s': lambda a, p: self.spin(a, p),
                     'x': lambda a, p: self.exchange(*a, p),
                     'p': lambda a, p: self.partner(*a, p)}
        self.ops = ops
        self.find_cycle()

    def spin(self, n, p):
        p[:n], p[n:] = p[-n:], p[:-n]

    def exchange(self, x, y, p):
        p[x], p[y] = p[y], p[x]

    def partner(self, v1, v2, p):
        self.exchange(p.index(v1), p.index(v2), p)

    def find_cycle(self):
        p, self.ident = list(self.progs), 0
        while True:
            self.ident += 1
            self.apply(p)
            if ''.join(p) == self.progs:
                break

    def apply(self, p):
        for op in self.ops:
            self.fcnt[op[0]](op[1], p)

    def apply_n(self, iters):
        p = list(self.progs)
        for _ in range(iters % self.ident):
            self.apply(p)
        return ''.join(p)


oper = Operator(ops)
print("Solutions: [{}] [{}]".format(
    oper.apply_n(1), oper.apply_n(1000000000)))
