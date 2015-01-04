#!/usr/bin/env python
# -*- coding: utf-8 -*-

evilpatterns = [
    ["(?<!BIKE|RAIL|REET)CAAAAA+R", "cars"],
    ["HYPERLOO+P", "hyperloop"],
]

asciipatterns = ["CALTRAAAAA+IN",
"TRAAA+IN",
"TERRAAA+IN",
"PLAAAA+NE",
"BOAAA+T", 
"BUUU+S",
"BRAAA+IN",
"SPAAA+IN",
"(?<!\w)Y+O+(?!\w)",
"BIII+KE",
"MAAA+INE",
"PLANTAAA+IN",
"PARAAA+DE",
"DUUU+CK", 
"BRIII+DGE",
"BAAA+RT",
"TYYY+PES",
"DAAA+RT",
"TGVVV+",
"RAILYAAA+RD",
"RAILCAAA+R",
"STREETCAAA+R",
"MUUU+NI",
"[Ii] propose"] # please keep this last

def load(filename):
   lines = [x.decode('utf8').rstrip() for x in open(filename).readlines()]
   third = len(lines)/3
   return [ lines[0:third], lines[third:2*third], lines[2*third:] ]

asciis=[
[['           __________________________________________', 
'       .--/__|_|____________________________________|', 
'       /     |-|         Cal\x0316,4train\x03            |.|  | |', 
'      /    __|-|_____________________________|_|__|_|', 
'     /____/<_>=<_>=<_>\_______________/<_>=<_>=<_>\_|='], [], []], 

[['                        (  ) (@@) ( )  (@)  ()    @@', 
'                   (@@@)', 
'               (    )', 
'            (@@@@)', 
'          (   )'], 
['      ====        ________                ___________', 
'  _D _|  |_______/        \__I_I_____===__|_________|', 
'   |(_)---  |   H\________/ |   |        =|___ ___|', 
'   /     |  |   H  |  |     |   |         ||_| |_||', 
'  |      |  |   H  |__--------------------| [___] |'], 
['  | ________|___H__/__|_____/[][]~\_______|       |', 
'  |/ |   |-----------I_____I [][] []  D   |=======|', 
'__/ =| o |=-~~\  /~~\  /~~\  /~~\ ____Y___________|', 
' |/-=|___|=O=====O=====O=====O   |_____/~\___/', 
'  \_/      \__/  \__/  \__/  \__/      \_/']], 

[["                                 _", 
"                       .-.      / \        _", 
"           ^^         /   \    /^./\__   _/ \ ", 
"         _        .--'\/\_ \__/.      \ /    \  ^^  ___", 
"        / \_    _/ ^      \/  __  :'   /\/\  /\  __/   \ "], 
["       /    \  /    .'   _/  /  \   ^ /    \/  \/ .`'\_/\ ", 
"      /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _", 
"     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \ ", 
"   /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \ ", 
"  /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  "], 
["@/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-", 
"@(88%@)@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8", 
"@88:::&(&8&&8::JGS:&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8", 
"`::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::", 
" `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"]], 

[["         _________", 
"         \        \ ", 
"          \        \               ___    __", 
"           \        \              \  \  / |", 
"           /\        \              \  \/  |"], 
["         O/  \ *****  \____________  \ /   |", 
"     \ /   ############## ***+++^^^^^^^\   \ ", 
"      X **################***+++^^^^^^^ \   \ ", 
"     / \   ############## ***+++^^^^^    \___\ ", 
"               / \       \          \o"], 
["             O/   \       \ ", 
"                   \       \ ", 
"                    \       \ ", 
"                     \       \ ", 
"                      \_______\ "]], 

[['       .  o ..                  ', 
'       o . o o.o                ', 
'            ...oo               ', 
'            ____[]____            ', 
'         __|_o_o_o_o_o\__  '], 
['''         \\""""""""""""""/         ''', 
'          \. ......  . /          ', 
'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'], []], 

[['          ____________________', 
'         / {)][o>][_o][c_][o][|', 
'        |-==)|                |', 
'        &_____________________L', 
'          ( )            ( )'], [], []], 

[['''                   __, --""""""""--, .''', 
'''            __, -'"                 _\ ^-, __''', 
'''         , -^                 /    \         \_''', 
'''       , '                   /_    |           \ ''', 
'''      /           _____, --""     /         )   \ '''], 
['''     /           /              /         (     |''', 
'''    |         /                |                \ ''', 
'''    (     (_/\      )                /           \ ''', 
'''     \        \_          ___, ===="""    /        |''', 
'''      \                /"               /""       |'''], 
['''       \_          _, -" |__, -'--------'"          |''', 
'''         "`------""   --"                , -'      /''', 
'''                \___/         __, -----, ___       )''', 
'''                    \    , --'"============""""-'"''', 
'''                     "-'" |  |================/''']], 

[['''  .,_.,,._,.,,,, ''',
''' {         ',.'` ''',
'''  ``}      : ''',
'''    (      ,' ''',
'''    |      /'''],
['''    `\____/'''], []], 

[["YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"], 
["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"], 
["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"]],

[[" .._\ ",
"(o)(o)"],[],[]],

[['                                     |__',
'                                     |\/',
'                                     ---',
'                                     / | [',
'                              !      | |||'],
['                            _/|     _/|-++',
'                        +  +--|    |--|--|_ |-',
'                     { /|__|  |/\__|  |--- |||__/',
'''                    +---------------___[}-_===_.'____                 /\ ''',
'''                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _'''],
[''' __..._____--==/___]_|__|_____________________________[___\==--____,------' .7''',
'''|                                                              USS MAINE   /''',
''' \_________________________________________________________________________|''']],

[['''//\ ''',
'''V  \ ''',
''' \  \_''',
'''  \,'.`-.''',
'''   |\ `. `.       '''],
['''   ( \  `. `-.                        _,.-:\ ''',
'''    \ \   `.  `-._             __..--' ,-';/''',
'''     \ `.   `-.   `-..___..---'   _.--' ,'/''',
'''      `. `.    `-._        __..--'    ,' /''',
'''        `. `-_     ``--..''       _.-' ,' '''],
['''          `-_ `-.___        __,--'   ,' ''',
'''             `-.__  `----"""    __.-' ''',
'''                  `--..____..--' ''']],

[
   ['   .    *   __#_#_#__    *   .  *  .-\'"\'-.     *      *    .      .  *         ',
    '*       .  {_` ` ` `_} .    .-\'"\'-/ #     \        *   .     *  .      *       ',
    '   *      _{_._._._._}_   ./ #   : #       : *  _____________                  '],
   ['.     *  {_           _}  ; #     \       /    /       /   \  \   ._           ',
    '        _{_._._._._._._}_  \       \     /    |       |      n \_/ ^ `\        ',
    ' *     {_               _}  \     / `\'p\'` .  /|               ___./ `\_|       '],
   ['   .---{_._._._._._._._._}---.\'p\'`    )     / \     /___|    /     *           ',
    '  (   `"""""""""""""""""""`   ))  *   (    "   |    |   |    |   .             ',
    '*  `~~~/^\~~~~~~~~~~~~~/^\~~~` (      )      . `____|   `____|        *        ']
],

[['''                    _ ''',
'''                  /`6\__ ''',
'''           ,_     \ _.==' ''',
'''          `) `""""`~~\ ''',
'''        -~ \  '~-.   / ~-'''],
['''         ~- `~-====-' ~_ ~- ''',
'''       ~ - ~ ~- ~ - ~ - '''],[]],

[['''              ..                                       ..''',
  '''              []                                       []''',
  '''            .:[]:_                                   ,:[]:.''',
  '''          .: :[]: :-.                             ,-: :[]: :.''',
  '''        .: : :[]: : :`._                       ,.': : :[]: : :.'''],
 ['''      .: : : :[]: : : : :-._               _,-: : : : :[]: : : :.''',
  '''  _..: : : : :[]: : : : : : :-._________.-: : : : : : :[]: : : : :-._''',
  '''  _:_:_:_:_:_:[]:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:[]:_:_:_:_:_:_''',
  '''  !!!!!!!!!!!![]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![]!!!!!!!!!!!!!''',
  '''  ^^^^^^^^^^^^[]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[]^^^^^^^^^^^^^'''],
 ['''              []                                       []''',
  '''              []                                       []''',
  '''              []                                       []''']],

[['       ______________________________________________________',
  '      /      ___________   ___________        _________',
  '     //|    |           | |           |      | __ | __ |',
  '    // |    |           | |           |  \x032b\x0312a\x03  ||  |||  ||',
  '   //  |    |           | |           |      ||  |||  ||'],
 ['  //___|    |___________| |___________|      ||__|||__||',
  ' / \x030,121254\x03\x032======================================\x03|    |    |\x032=====\x03',
  '/____________________________________________|____|____|_____',
  '\\',
  ' \___________________________________________________________'],
 ['        |_______|    |  o  |____________|  o  |     |______|',
  '                      \___/              \___/']],

[[u'''                                                            ''',
  u'''    x : σ ∈ Γ                  Γ, x : σ ⊢ e : τ             ''',
  u'''    ───────── (T-VAR)     ────────────────────────── (T-ABS)''',
  u'''    Γ ⊢ x : σ             Γ ⊢ (λx : σ . e) : (σ → τ)        ''',
  u'''                                                            '''],
 [u'''                                                            ''',
  u'''            Γ ⊢ e₁ : σ → τ   Γ ⊢ e₂ : σ                     ''',
  u'''            ─────────────────────────── (T-APP)             ''',
  u'''                   Γ ⊢ e₁ e₂ : τ                            ''',
  u'''                                                            '''], []],
  
[[' ____________________________________________________________',
  '|  _____     ____________ _____________       __________',
  '|  |   |    |           | |           |      | __ | __ |',
  '|  |   |    |           | |           |DART25||  |||  ||',
  '|  |   |    |           | |           |      ||  |||  ||'],
 ['|  |___|    |___________| |___________|      ||__|||__||',
  '|                                            |    |    |',
  '|____________________________________________|____|____|_____',
  '''|''',
  '| ____________________________________________________________'],
 ['        |_______|    |  o  |____________|  o  |     |______|',
  '                      \___/              \___/']],

 load("asciis/tgv.txt"),

 load("asciis/railyard.txt"),

 load("asciis/railcar.txt"),

 load("asciis/streetcar.txt"),

[['          ____________________', 
'         / {)][o>][_o][c_][o][|', 
'        |-==)|     MUNI       |', 
'        &_____________________L', 
'          ( )            ( )'], [], []], 

[["Splendid!"],["Splendid!"],[]]

]
