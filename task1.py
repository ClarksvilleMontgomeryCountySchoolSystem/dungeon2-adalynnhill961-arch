good = r"""

                                                      _--_     dMb
                                                   __(._  )   d0P
                                                     <  (D)  .MP
                                                   .~ \ /~```M-.
                                                 .~    V    Mo_ \

          -------============((((}{)             (   (___. {:)-./
                                                  ~._____.(:}
                                  '94 the wolfe    /     .M\
                                                  /      "" \
                                                  |    /\   |
                                                  /   /  \   \
                                                 /   /    \   \
                                                 \__/      \__/
                                                 / /        | |
                                                .^V^.      .^V^.
                                                 +-+        +-+

"""
bad = r"""
    _)\_      _..--'O"o\-.
  /e  ,`--o'O  o O' 0 o|.`o-._
<_, ; o 0 o" O "_.\ o(  `-._o``--..___..-o')
  --' `, o/,--''' _/O,';     ``-o..o___o--''
    _,'o,'/      (,.'-'
   (,.-'-'
fl/tbk
"""
torch_lit = False
if torch_lit:
    outcome = "Flicker: I can see!"
    print(good)
else:
    outcome = "Doom: It's hard to see!"
    print(bad)
print(outcome)

